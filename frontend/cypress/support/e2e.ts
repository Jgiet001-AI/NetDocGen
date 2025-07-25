// Cypress E2E support file
import './commands';

// Disable uncaught exception handling
Cypress.on('uncaught:exception', (err, runnable) => {
  // Return false to prevent the error from failing the test
  return false;
});

// Add custom types
declare global {
  namespace Cypress {
    interface Chainable {
      login(email: string, password: string): Chainable<void>;
      logout(): Chainable<void>;
      uploadFile(fileName: string, selector: string): Chainable<void>;
      waitForProcessing(timeout?: number): Chainable<void>;
    }
  }
}

// Prevent TypeScript from reading file as legacy script
export {};