describe('Project Management', () => {
  beforeEach(() => {
    cy.login('test@example.com', 'password123');
    cy.visit('/projects');
  });

  it('should create a new project', () => {
    cy.intercept('POST', '**/api/v1/projects', {
      statusCode: 201,
      body: {
        id: 'proj-123',
        name: 'Network Upgrade 2024',
        description: 'Company network infrastructure upgrade',
        created_at: new Date().toISOString(),
      },
    }).as('createProject');

    cy.get('[data-testid="create-project-button"]').click();
    cy.get('[data-testid="project-modal"]').should('be.visible');

    cy.get('input[name="name"]').type('Network Upgrade 2024');
    cy.get('textarea[name="description"]').type('Company network infrastructure upgrade');
    cy.get('[data-testid="submit-project"]').click();

    cy.wait('@createProject');
    cy.get('[data-testid="project-proj-123"]').should('contain', 'Network Upgrade 2024');
  });

  it('should list and filter projects', () => {
    cy.intercept('GET', '**/api/v1/projects', {
      statusCode: 200,
      body: [
        {
          id: 'proj-1',
          name: 'Data Center Network',
          description: 'Main data center documentation',
          created_at: '2024-01-01T00:00:00Z',
        },
        {
          id: 'proj-2',
          name: 'Branch Office Setup',
          description: 'Branch office network setup',
          created_at: '2024-01-02T00:00:00Z',
        },
      ],
    }).as('getProjects');

    cy.visit('/projects');
    cy.wait('@getProjects');

    // Check all projects are displayed
    cy.get('[data-testid^="project-"]').should('have.length', 2);

    // Filter projects
    cy.get('[data-testid="search-projects"]').type('Data Center');
    cy.get('[data-testid^="project-"]').should('have.length', 1);
    cy.get('[data-testid="project-proj-1"]').should('be.visible');
  });

  it('should add documents to project', () => {
    cy.visit('/projects/proj-123');

    cy.intercept('GET', '**/api/v1/projects/proj-123', {
      statusCode: 200,
      body: {
        id: 'proj-123',
        name: 'Network Upgrade 2024',
        description: 'Company network infrastructure upgrade',
        documents: [],
      },
    }).as('getProject');

    cy.intercept('POST', '**/api/v1/projects/proj-123/documents', {
      statusCode: 200,
      body: {
        message: 'Document added successfully',
      },
    }).as('addDocument');

    cy.wait('@getProject');

    // Add document to project
    cy.get('[data-testid="add-document-button"]').click();
    cy.get('[data-testid="document-select"]').select('doc-123');
    cy.get('[data-testid="add-document-submit"]').click();

    cy.wait('@addDocument');
    cy.get('[data-testid="success-message"]').should('contain', 'Document added successfully');
  });

  it('should update project details', () => {
    cy.visit('/projects/proj-123');

    cy.intercept('PUT', '**/api/v1/projects/proj-123', {
      statusCode: 200,
      body: {
        id: 'proj-123',
        name: 'Network Upgrade 2024 - Updated',
        description: 'Updated description',
      },
    }).as('updateProject');

    cy.get('[data-testid="edit-project-button"]').click();
    cy.get('input[name="name"]').clear().type('Network Upgrade 2024 - Updated');
    cy.get('textarea[name="description"]').clear().type('Updated description');
    cy.get('[data-testid="save-project"]').click();

    cy.wait('@updateProject');
    cy.get('[data-testid="project-name"]').should('contain', 'Network Upgrade 2024 - Updated');
  });

  it('should delete project with confirmation', () => {
    cy.visit('/projects/proj-123');

    cy.intercept('DELETE', '**/api/v1/projects/proj-123', {
      statusCode: 204,
    }).as('deleteProject');

    cy.get('[data-testid="delete-project-button"]').click();
    cy.get('[data-testid="confirm-dialog"]').should('be.visible');
    cy.get('[data-testid="confirm-delete"]').click();

    cy.wait('@deleteProject');
    cy.url().should('include', '/projects');
    cy.get('[data-testid="success-message"]').should('contain', 'Project deleted');
  });
});