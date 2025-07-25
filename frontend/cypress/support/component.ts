// Cypress component testing support file
import './commands';

// Import global styles if needed
// import '../../src/styles/globals.css';

// Mount helper for React components
import { mount } from 'cypress/react18';

declare global {
  namespace Cypress {
    interface Chainable {
      mount: typeof mount;
    }
  }
}

Cypress.Commands.add('mount', mount);