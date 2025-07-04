import asyncio
from playwright.async_api import async_playwright
from playwright._impl._api_structures import (
    PdfMargins,
)
async def url_to_pdf(url, output_path):
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto(url)
        await page.pdf(
            path=output_path,
            format='A4',
            margin=PdfMargins(top='1.4cm', bottom='1.5cm', left='1cm', right='1cm'),
            display_header_footer=True,
            header_template="<div></div>",
            footer_template="""
                <div style="width: 100%; text-align: right; font-size: 10px; margin-right: 20px;">
                    Page <span class="pageNumber"></span> of
                    <span class="totalPages"></span>
                    <div class="title"></div>
                </div>
            """
        )
        await browser.close()

# Example usage
url = 'http://localhost:8080/tenancy_agreement_template.html'
output_path = 'tenancy_agreement.pdf'

asyncio.run(url_to_pdf(url, output_path))
