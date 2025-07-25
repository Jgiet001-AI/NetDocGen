// Custom Cypress commands

// Login command
Cypress.Commands.add('login', (email: string, password: string) => {
  cy.request('POST', `${Cypress.env('API_URL')}/api/v1/auth/login`, {
    email,
    password,
  }).then((response) => {
    window.localStorage.setItem('authToken', response.body.access_token);
    window.localStorage.setItem('refreshToken', response.body.refresh_token);
    window.localStorage.setItem('user', JSON.stringify(response.body.user));
  });
});

// Logout command
Cypress.Commands.add('logout', () => {
  window.localStorage.removeItem('authToken');
  window.localStorage.removeItem('refreshToken');
  window.localStorage.removeItem('user');
});

// File upload command
Cypress.Commands.add('uploadFile', (fileName: string, selector: string) => {
  cy.fixture(fileName, 'base64').then((fileContent) => {
    cy.get(selector).attachFile({
      fileContent,
      fileName,
      mimeType: 'application/vnd.ms-visio.drawing',
      encoding: 'base64',
    });
  });
});

// Wait for document processing
Cypress.Commands.add('waitForProcessing', (timeout = 30000) => {
  cy.get('[data-testid="processing-status"]', { timeout }).should(
    'contain',
    'completed'
  );
});