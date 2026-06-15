# AidFastBD Test Strategy (AT-level)

## Objective
Deliver an acceptance-level test automation suite that validates the AidFast homepage and primary service navigation points, ensuring the site is available and key user journeys function correctly.

## Scope
- Homepage accessibility and page title validation
- Core navigation from homepage to service pages
- Presence of key homepage sections, including service cards and contact form
- Stability of the main call-to-action buttons and navigation links

## Test Levels
- AT (Acceptance Testing): End-to-end user-facing checks executed against the production web pages.
- No unit or API-level tests are included in this suite.

## Test Strategy
1. Smoke tests
   - Verify the homepage loads successfully with HTTP 200.
   - Verify the page title and key visible sections are present.
2. Navigation flows
   - Verify links for primary service categories navigate to correct service URLs.
   - Verify the `লগ ইন` link directs to `/registration`.
   - Verify the footer links navigate to privacy and terms pages.
3. Content validation
   - Verify the homepage includes the main service header `AidFast এর সেবাসমূহ`.
   - Verify the contact form fields are present and visible.
4. Non-functional checks
   - Validate the homepage renders without fatal JavaScript errors.
   - Validate website title matches expected brand text.

## Risks and Assumptions
- The site content is primarily localized in Bengali; selectors use text and URL targets to remain stable.
- Changes to the homepage structure may require selector updates.
- The automation suite is designed for Chromium headless execution but can be adapted to additional browsers.

## Acceptance Criteria
- All tests execute successfully in the Playwright environment.
- The homepage returns a valid title and response.
- Primary service navigation buttons lead to correct URLs.
- Contact form fields are rendered on the homepage.

## Test Data
No external data sources are required. Tests rely on page navigation and verified static content available from the homepage.
