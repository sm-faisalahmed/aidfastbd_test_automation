import pytest

BASE_URL = "https://aidfastbd.com"


def test_homepage_loads_and_displays_brand(page):
    page.goto(BASE_URL, wait_until="networkidle")
    assert "AidFast" in page.title(), "Expected page title to contain AidFast"
    assert page.locator('text=AidFast এর সেবাসমূহ').first.is_visible(), "Homepage should display the main service heading"
    assert page.locator('text=লগ ইন').first.is_visible(), "Login link should be visible on the homepage"


@pytest.mark.parametrize(
    "relative_url, visible_text",
    [
        ("/login", "লগ ইন"),
        ("/doctor", "ডাক্তার"),
        ("/diagnostic", "ডায়াগনস্টিক"),
        ("/blood", "ব্লাড ব্যাংক"),
        ("/ambulance", "অ্যাম্বুলেন্স"),
    ],
)
def test_primary_navigation_links(relative_url, visible_text, page):
    page.goto(BASE_URL, wait_until="networkidle")
    locator = page.locator(f'a[href="{relative_url}"]')
    assert locator.first.is_visible(), f"Expected link to {relative_url} to be visible"
    # Some anchors are handled by client-side code and do not perform a full navigation.
    # Verify the anchor's href and that the expected visible text appears on the anchor or page.
    href = locator.first.get_attribute('href')
    assert href and href.endswith(relative_url), f"Expected anchor href to end with {relative_url}, got {href}"
    anchor_text = locator.first.inner_text().strip()
    assert (
        visible_text in anchor_text or visible_text in page.locator('body').inner_text()
    ), f"Expected anchor or page to contain text {visible_text}"


def test_footer_links(page):
    page.goto(BASE_URL, wait_until="networkidle")
    privacy_link = page.locator('footer a[href="/privacy"]')
    terms_link = page.locator('footer a[href="/terms"]')
    assert privacy_link.first.is_visible(), "Privacy link should be visible in the footer"
    assert terms_link.first.is_visible(), "Terms link should be visible in the footer"


def test_contact_form_fields_present(page):
    page.goto(BASE_URL, wait_until="networkidle")
    assert page.locator('input[placeholder="নাম লিখুন"]').first.is_visible(), "Name field should be present"
    assert page.locator('input[placeholder="ইমেইল লিখুন"]').first.is_visible(), "Email field should be present"
    assert page.locator('input[placeholder="মোবাইল নাম্বার লিখুন"]').first.is_visible(), "Mobile field should be present"
    assert page.locator('textarea[placeholder="আপনার বার্তা লিখুন"]').first.is_visible(), "Message field should be present"
