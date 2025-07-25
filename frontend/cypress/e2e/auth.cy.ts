describe('Authentication', () => {
  beforeEach(() => {
    cy.visit('/');
  });

  it('should display login form', () => {
    cy.get('[data-testid="login-form"]').should('be.visible');
    cy.get('input[name="email"]').should('be.visible');
    cy.get('input[name="password"]').should('be.visible');
    cy.get('button[type="submit"]').should('contain', 'Login');
  });

  it('should show validation errors for empty fields', () => {
    cy.get('button[type="submit"]').click();
    cy.get('[data-testid="error-message"]').should('contain', 'required');
  });

  it('should login with valid credentials', () => {
    cy.intercept('POST', '**/api/v1/auth/login', {
      statusCode: 200,
      body: {
        access_token: 'fake-token',
        refresh_token: 'fake-refresh',
        token_type: 'bearer',
        user: {
          id: '123',
          email: 'test@example.com',
          full_name: 'Test User',
        },
      },
    }).as('login');

    cy.get('input[name="email"]').type('test@example.com');
    cy.get('input[name="password"]').type('password123');
    cy.get('button[type="submit"]').click();

    cy.wait('@login');
    cy.url().should('include', '/dashboard');
    cy.get('[data-testid="user-menu"]').should('contain', 'Test User');
  });

  it('should show error for invalid credentials', () => {
    cy.intercept('POST', '**/api/v1/auth/login', {
      statusCode: 401,
      body: {
        detail: 'Invalid credentials',
      },
    }).as('loginFail');

    cy.get('input[name="email"]').type('wrong@example.com');
    cy.get('input[name="password"]').type('wrongpassword');
    cy.get('button[type="submit"]').click();

    cy.wait('@loginFail');
    cy.get('[data-testid="error-message"]').should('contain', 'Invalid credentials');
  });

  it('should register new user', () => {
    cy.get('a[href="/register"]').click();
    cy.url().should('include', '/register');

    cy.intercept('POST', '**/api/v1/auth/register', {
      statusCode: 201,
      body: {
        id: '456',
        email: 'newuser@example.com',
        full_name: 'New User',
      },
    }).as('register');

    cy.get('input[name="fullName"]').type('New User');
    cy.get('input[name="email"]').type('newuser@example.com');
    cy.get('input[name="password"]').type('newpassword123');
    cy.get('input[name="confirmPassword"]').type('newpassword123');
    cy.get('button[type="submit"]').click();

    cy.wait('@register');
    cy.url().should('include', '/login');
    cy.get('[data-testid="success-message"]').should('contain', 'Registration successful');
  });

  it('should logout user', () => {
    // First login
    cy.login('test@example.com', 'password123');
    cy.visit('/dashboard');

    cy.get('[data-testid="user-menu"]').click();
    cy.get('[data-testid="logout-button"]').click();

    cy.url().should('include', '/login');
    cy.window().then((win) => {
      expect(win.localStorage.getItem('authToken')).to.be.null;
      expect(win.localStorage.getItem('user')).to.be.null;
    });
  });
});