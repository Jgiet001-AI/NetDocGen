describe('Document Processing Flow', () => {
  beforeEach(() => {
    cy.login('test@example.com', 'password123');
    cy.visit('/dashboard');
  });

  it('should complete full document processing flow', () => {
    // Navigate to documents page
    cy.get('[data-testid="nav-documents"]').click();
    cy.url().should('include', '/documents');

    // Click upload button
    cy.get('[data-testid="upload-button"]').click();

    // Mock file upload
    cy.intercept('POST', '**/api/v1/documents/upload', {
      statusCode: 200,
      body: {
        id: 'doc-123',
        filename: 'network-diagram.vsdx',
        status: 'pending',
        created_at: new Date().toISOString(),
      },
    }).as('upload');

    // Upload file
    cy.get('input[type="file"]').selectFile({
      contents: Cypress.Buffer.from('fake-visio-content'),
      fileName: 'network-diagram.vsdx',
      mimeType: 'application/vnd.ms-visio.drawing',
    });

    cy.wait('@upload');

    // Mock processing status updates
    cy.intercept('GET', '**/api/v1/documents/doc-123', (req) => {
      req.reply({
        statusCode: 200,
        body: {
          id: 'doc-123',
          filename: 'network-diagram.vsdx',
          status: 'processing',
          created_at: new Date().toISOString(),
        },
      });
    }).as('getProcessing');

    // Check processing status
    cy.get('[data-testid="document-doc-123"]').should('be.visible');
    cy.get('[data-testid="status-doc-123"]').should('contain', 'processing');

    // Update to completed status
    cy.intercept('GET', '**/api/v1/documents/doc-123', {
      statusCode: 200,
      body: {
        id: 'doc-123',
        filename: 'network-diagram.vsdx',
        status: 'completed',
        created_at: new Date().toISOString(),
        parsed_data: {
          shapes: 10,
          connections: 15,
        },
      },
    }).as('getCompleted');

    // Wait for completion
    cy.wait(2000); // Simulate processing time
    cy.get('[data-testid="refresh-button"]').click();
    cy.wait('@getCompleted');

    cy.get('[data-testid="status-doc-123"]').should('contain', 'completed');

    // Click to view details
    cy.get('[data-testid="view-doc-123"]').click();
    cy.url().should('include', '/documents/doc-123');

    // Check document details
    cy.get('[data-testid="document-title"]').should('contain', 'network-diagram.vsdx');
    cy.get('[data-testid="shape-count"]').should('contain', '10');
    cy.get('[data-testid="connection-count"]').should('contain', '15');

    // Generate documentation
    cy.get('[data-testid="generate-button"]').click();
    cy.get('[data-testid="format-select"]').select('pdf');

    cy.intercept('POST', '**/api/v1/documents/doc-123/generate', {
      statusCode: 200,
      body: {
        download_url: '/api/v1/documents/doc-123/download?format=pdf',
      },
    }).as('generate');

    cy.get('[data-testid="generate-submit"]').click();
    cy.wait('@generate');

    // Check download link
    cy.get('[data-testid="download-link"]').should('be.visible');
  });

  it('should enhance document with AI', () => {
    // Navigate to existing document
    cy.visit('/documents/doc-123');

    // Mock AI enhancement
    cy.intercept('POST', '**/api/v1/analysis/documents/doc-123/enhance', {
      statusCode: 200,
      body: {
        document_id: 'doc-123',
        enhancements: {
          executive_summary: 'This network consists of...',
          glossary: [
            { term: 'Router', definition: 'A network device...' },
          ],
          suggested_sections: [
            { title: 'Overview', description: 'Network overview...' },
          ],
        },
      },
    }).as('enhance');

    // Click AI enhance button
    cy.get('[data-testid="ai-enhance-button"]').click();
    cy.wait('@enhance');

    // Check AI enhancements are displayed
    cy.get('[data-testid="ai-summary"]').should('contain', 'This network consists of');
    cy.get('[data-testid="ai-glossary"]').should('contain', 'Router');
    cy.get('[data-testid="ai-sections"]').should('contain', 'Overview');
  });

  it('should handle document errors gracefully', () => {
    // Mock failed upload
    cy.intercept('POST', '**/api/v1/documents/upload', {
      statusCode: 500,
      body: {
        detail: 'Server error occurred',
      },
    }).as('uploadError');

    cy.get('[data-testid="upload-button"]').click();
    cy.get('input[type="file"]').selectFile({
      contents: Cypress.Buffer.from('fake-content'),
      fileName: 'bad-file.vsdx',
    });

    cy.wait('@uploadError');
    cy.get('[data-testid="error-message"]').should('contain', 'Server error occurred');
  });
});