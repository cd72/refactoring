import pytest
from refactoring.statement import statement

@pytest.fixture
def plays():
    return {
        "hamlet": {"name": "Hamlet", "type": "tragedy"},
        "as-like": {"name": "As You Like It", "type": "comedy"},
        "othello": {"name": "Othello", "type": "tragedy"},
    }

@pytest.fixture
def statement1():
    return {
            "customer": "BigCo",
            "performances": [
                {"playID": "hamlet",
                    "audience": 55},
                    {"playID": "as-like",
                    "audience": 35},
                    {"playID": "othello",
                    "audience": 40},
            ],
        }

@pytest.fixture
def statement2():
    return {
            "customer": "SmallCo",
            "performances": [
                {"playID": "hamlet",
                    "audience": 30},
                    {"playID": "as-like",
                    "audience": 20},
                    {"playID": "othello",
                    "audience": 10},
            ],
        }


@pytest.fixture
def zero_audience():
    return {
            "customer": "ZeroCo",
            "performances": [
                {"playID": "hamlet",
                    "audience": 0},
                    {"playID": "as-like",
                    "audience": 0},
                    {"playID": "othello",
                    "audience": 0},
            ],
        }

@pytest.fixture
def no_performances():
    return {
            "customer": "NoCo",
            "performances": [],
        }

class TestStatement1:
    @pytest.fixture(autouse=True)
    def generate_statement(self, statement1, plays):
        self.result = statement(statement1, plays)
        self.result_lines = self.result.split("\n")

    def test_statement_title(self):
        assert self.result.startswith("Statement for BigCo")

    def test_statement_hamlet(self):
        assert "  Hamlet: $650.00 (55 seats)" in self.result_lines

    def test_statement_as_like(self):
        assert "  As You Like It: $580.00 (35 seats)" in self.result_lines

    def test_statement_othello(self):
        assert "  Othello: $500.00 (40 seats)" in self.result_lines

    def test_statement_total_amount(self):
        assert "Amount owed is $1,730.00" in self.result_lines

    def test_statement_volume_credits(self):
        assert self.result.endswith("You earned 47 credits\n")

class TestStatement2:
    @pytest.fixture(autouse=True)
    def generate_statement(self, statement2, plays):
        self.result = statement(statement2, plays)
        self.result_lines = self.result.split("\n")

    def test_statement_title(self):
        assert self.result.startswith("Statement for SmallCo")

    def test_statement_hamlet(self):
        assert "  Hamlet: $400.00 (30 seats)" in self.result_lines

    def test_statement_as_like(self):
        assert "  As You Like It: $360.00 (20 seats)" in self.result_lines

    def test_statement_othello(self):
        assert "  Othello: $400.00 (10 seats)" in self.result_lines

    def test_statement_total_amount(self):
        assert "Amount owed is $1,160.00" in self.result_lines

    def test_statement_volume_credits(self):
        assert self.result.endswith("You earned 4 credits\n")

class TestZeroAudience:
    @pytest.fixture(autouse=True)
    def generate_statement(self, zero_audience, plays):
        self.result = statement(zero_audience, plays)
        self.result_lines = self.result.split("\n")

    def test_statement_title(self):
        assert self.result.startswith("Statement for ZeroCo")

    def test_statement_hamlet(self):
        assert "  Hamlet: $400.00 (0 seats)" in self.result_lines

    def test_statement_as_like(self):
        assert "  As You Like It: $300.00 (0 seats)" in self.result_lines

    def test_statement_othello(self):
        assert "  Othello: $400.00 (0 seats)" in self.result_lines

    def test_statement_total_amount(self):
        assert "Amount owed is $1,100.00" in self.result_lines

    def test_statement_volume_credits(self):
        assert self.result.endswith("You earned 0 credits\n")

class TestNoPerformances:
    @pytest.fixture(autouse=True)
    def generate_statement(self, no_performances, plays):
        self.result = statement(no_performances, plays)
        self.result_lines = self.result.split("\n")

    def test_statement_title(self):
        assert self.result.startswith("Statement for NoCo")

    def test_statement_total_amount(self):
        assert "Amount owed is $0.00" in self.result_lines

    def test_statement_volume_credits(self):
        assert self.result.endswith("You earned 0 credits\n")