import pytest
from google_finance import GoogleFinance


class TestGoogleFinance:
    TEST_STOCKS = {"NFLX", "MSFT", "TSLA"}

    @pytest.fixture(scope="class")
    def finance(self):
        # Setup and instantiate the GoogleFinance class
        gf = GoogleFinance()
        gf.setup()
        # Assert that the correct web page has been loaded
        assert gf.driver.title == gf.title
        # Pass the web driver wrapper class to the test
        yield gf
        # Teardown: Quit the WebDriver after the tests
        gf.teardown()

    # Instruction #3
    @pytest.mark.all
    def test_get_all_ymbi_stock_names(self, finance):
        # Act
        stock_names = finance.get_you_may_be_interested_in_stock_names()

        # Print
        print(f"Stock names found: {stock_names}")

        # Assert
        assert len(stock_names) == 6  # At least one stock name should be found

    # Instruction #5
    @pytest.mark.all
    @pytest.mark.instruction_5_and_6
    def test_get_ymbi_stock_names_not_present_in_test_stocks(self, finance):
        # Act
        stock_names = finance.get_you_may_be_interested_in_stock_names()
        reduced_stocks = set(stock_names) - self.TEST_STOCKS

        # Print
        print(f"Stock names found: {reduced_stocks}")

        # Assert
        assert len(reduced_stocks) > 0

    # Instruction #6
    @pytest.mark.all
    @pytest.mark.instruction_5_and_6
    def test_get_which_test_stocks_are_not_present_in_ymbi_section(self, finance):
        # Act
        stock_names = finance.get_you_may_be_interested_in_stock_names()
        reduced_stocks = self.TEST_STOCKS - set(stock_names)

        # Print
        print(f"Stock names found: {reduced_stocks}")

        # Assert
        assert len(reduced_stocks) <= 3


# If you are running the tests directly
if __name__ == "__main__":
    pytest.main()