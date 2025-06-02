from datetime import date
from typing import List, Optional, Union

from rich import print
from openai import OpenAI
from pydantic import BaseModel, EmailStr, Field


class PersonalDetails(BaseModel):
    """Personal details of an individual client"""

    first_name: Optional[str] = Field(None, description="First name of the client")
    last_name: Optional[str] = Field(None, description="Last name of the client")
    middle_name: Optional[str] = Field(
        None, description="Middle name of the client (if any)"
    )
    date_of_birth: Optional[date] = Field(
        None, description="Date of birth in ISO format (YYYY-MM-DD)"
    )
    marital_status: Optional[str] = Field(
        None, description="Marital status of the client"
    )
    title: Optional[str] = None
    known_as: Optional[str] = Field(None, description="Known as of the client (if any)")
    pronoun: Optional[str] = Field(None, description="Pronoun of the client")
    gender: Optional[str] = Field(None, description="Gender of the client")
    legal_sex: Optional[str] = Field(None, description="Legal sex of the client")
    place_of_birth: Optional[str] = Field(
        None, description="Place of birth of the client"
    )
    email: Optional[EmailStr] = Field(None, description="Email address of the client")
    mobile_phone: Optional[str] = Field(
        None, description="Mobile phone number of the client"
    )


class Employment(BaseModel):
    """Employment details of an individual client"""

    occupation: Optional[str] = Field(None, description="Occupation of the client")
    employer: Optional[str] = Field(None, description="Employer name")
    employment_status: Optional[str] = Field(
        None, description="Employment status (full-time, part-time, etc.)"
    )
    desired_retirement_age: Optional[int] = Field(
        None, description="Desired retirement age"
    )
    employment_started: Optional[date] = Field(
        None, description="Date employment started"
    )
    country_domiciled: Optional[str] = Field(None, description="Country of domicile")
    tax_resident: Optional[str] = Field(None, description="Country of tax residence")
    national_insurance_number: Optional[str] = Field(
        None, description="National Insurance number"
    )
    highest_tax_rate: Optional[str] = Field(
        None, description="Highest rate of tax paid"
    )


class Income(BaseModel):
    """Individual income item"""

    owner: Optional[str] = Field(
        None, description="Who owns this income (Client1, Client2, Joint)"
    )
    name: Optional[str] = Field(None, description="Name/type of income")
    amount: Optional[float] = Field(None, description="Income amount")
    frequency: Optional[str] = Field(
        None, description="Income frequency (Annual, Monthly, etc.)"
    )
    net_gross: Optional[str] = Field(None, description="Whether amount is net or gross")
    timeframe: Optional[str] = Field(None, description="Timeframe for this income")


class Expense(BaseModel):
    """Individual expense item"""

    owner: Optional[str] = Field(
        None, description="Who owns this expense (Client1, Client2, Joint)"
    )
    name: Optional[str] = Field(None, description="Name/type of expense")
    amount: Optional[float] = Field(None, description="Expense amount")
    frequency: Optional[str] = Field(
        None, description="Expense frequency (Annual, Monthly, etc.)"
    )
    priority: Optional[str] = Field(None, description="Priority level of expense")
    timeframe: Optional[str] = Field(None, description="Timeframe for this expense")
    notes: Optional[str] = Field(None, description="Additional notes about the expense")


class Pension(BaseModel):
    """Individual pension account"""

    owner: Optional[str] = Field(
        None, description="Who owns this pension (Client1, Client2, Joint)"
    )
    type: Optional[str] = Field(None, description="Type of pension account")
    provider: Optional[str] = Field(None, description="Pension provider")
    value: Optional[float] = Field(None, description="Current value of the pension")
    policy_number: Optional[str] = Field(None, description="Policy number")
    contributions: Optional[str] = Field(None, description="Contribution details")


class OtherAsset(BaseModel):
    """Other assets like property, inheritance, etc."""

    owner: Optional[str] = Field(
        None, description="Who owns this asset (Client1, Client2, Joint)"
    )
    description: Optional[str] = Field(None, description="Description of the asset")
    location: Optional[str] = Field(None, description="Location of the asset")
    current_value: Optional[float] = Field(
        None, description="Current value of the asset"
    )
    original_value: Optional[float] = Field(
        None, description="Original value of the asset"
    )
    mortgage_free: Optional[bool] = Field(
        None, description="Whether the asset is mortgage-free"
    )
    availability_date: Optional[date] = Field(
        None, description="When the asset becomes available"
    )


class Address(BaseModel):
    """Address information"""

    ownership_status: Optional[str] = Field(
        None, description="Ownership status (e.g., Owner, Tenant, Living with family)"
    )
    postcode: Optional[str] = Field(None, description="Postal/ZIP code")
    house_name_number: Optional[str] = Field(None, description="House name or number")
    street_name: Optional[str] = Field(None, description="Street name")
    address_line_3: Optional[str] = Field(None, description="Additional address line")
    address_line_4: Optional[str] = Field(None, description="Additional address line")
    town_city: Optional[str] = Field(None, description="Town or city")
    county: Optional[str] = Field(None, description="County or state")
    country: Optional[str] = Field(None, description="Country")
    move_in_date: Optional[date] = Field(
        None, description="Date moved into this address"
    )


class Dependant(BaseModel):
    """Dependant information"""

    name: Optional[str] = Field(None, description="Name of the dependant")
    date_of_birth: Optional[date] = Field(None, description="Date of birth")
    dependent_until: Optional[date] = Field(None, description="Date until dependent")


class HealthDetails(BaseModel):
    """Health details of the client"""

    current_state_of_health: Optional[str] = Field(
        None, description="Current state of health"
    )
    state_of_health_explanation: Optional[str] = Field(
        None, description="Detailed explanation of health state"
    )
    smoker: Optional[bool] = Field(None, description="Whether the client is a smoker")
    cigarettes_per_day: Optional[int] = Field(
        None, description="Number of cigarettes smoked per day"
    )
    smoker_since: Optional[date] = Field(None, description="Date when smoking started")
    long_term_care_needed: Optional[bool] = Field(
        None, description="Whether long term care is needed"
    )
    long_term_care_explanation: Optional[str] = Field(
        None, description="Explanation of long term care needs"
    )
    has_will: Optional[bool] = Field(None, description="Whether the client has a will")
    will_information: Optional[str] = Field(
        None, description="Information about the will"
    )
    power_of_attorney: Optional[bool] = Field(
        None, description="Whether there is a power of attorney"
    )
    power_of_attorney_details: Optional[str] = Field(
        None, description="Details of individual with power of attorney"
    )


class Objectives(BaseModel):
    """Retirement and financial objectives"""

    retirement_date: Optional[Union[date, str]] = Field(
        None, description="Target retirement date"
    )
    target_annual_income: Optional[float] = Field(
        None, description="Target annual retirement income"
    )
    breakdown: Optional[str] = Field(None, description="Breakdown of income sources")
    risk_tolerance: Optional[str] = Field(None, description="Risk tolerance level")
    key_goals: Optional[List[str]] = Field(
        None, description="List of key financial goals"
    )


class ExpenseCategories(BaseModel):
    """Categorized expenses"""

    loan_repayments: List[Expense] = Field(
        default_factory=list, description="Loan repayment expenses"
    )
    housing_expenses: List[Expense] = Field(
        default_factory=list, description="Housing-related expenses"
    )
    motoring_expenses: List[Expense] = Field(
        default_factory=list, description="Vehicle-related expenses"
    )
    personal_expenses: List[Expense] = Field(
        default_factory=list, description="Personal expenses"
    )
    professional_expenses: List[Expense] = Field(
        default_factory=list, description="Professional expenses"
    )
    miscellaneous_expenses: List[Expense] = Field(
        default_factory=list, description="Other expenses"
    )


class PersonalDetailsContainer(BaseModel):
    """Container for both clients' personal details"""

    client1: Optional[PersonalDetails] = Field(
        default_factory=PersonalDetails, description="Primary client details"
    )
    client2: Optional[PersonalDetails] = Field(
        default_factory=PersonalDetails, description="Secondary client details"
    )


class EmploymentContainer(BaseModel):
    """Container for both clients' employment details"""

    client1: Optional[Employment] = Field(
        default_factory=Employment, description="Primary client employment"
    )
    client2: Optional[Employment] = Field(
        default_factory=Employment, description="Secondary client employment"
    )


class HealthContainer(BaseModel):
    """Container for both clients' health details"""

    client1: Optional[HealthDetails] = Field(
        default_factory=HealthDetails, description="Primary client health"
    )
    client2: Optional[HealthDetails] = Field(
        default_factory=HealthDetails, description="Secondary client health"
    )


class FactFind(BaseModel):
    personal_details: Optional[PersonalDetailsContainer] = None
    employment: Optional[EmploymentContainer] = None
    current_address: Optional[Address] = None
    previous_addresses: List[Address] = Field(default_factory=list)
    dependants: List[Dependant] = Field(default_factory=list)
    incomes: List[Income] = Field(default_factory=list)
    expenses: Optional[ExpenseCategories] = None
    pensions: List[Pension] = Field(default_factory=list)
    other_assets: List[OtherAsset] = Field(default_factory=list)
    health: Optional[HealthContainer] = None
    objectives: Optional[Objectives] = None

    model_config = {"populate_by_name": True}

    @classmethod
    def json_schema(cls):
        """Return an OpenAI‑compatible JSON schema."""
        return cls.model_json_schema()


SYSTEM_PROMPT = """
You are an experienced paraplanner working for a regulated financial advisory firm. Your role is to extract and structure client information from meeting transcripts into a standardized Customer Information Form (CIF) format.

CORE RESPONSIBILITIES:
• Extract factual information explicitly stated in the transcript
• Structure data according to the provided JSON schema
• Maintain regulatory compliance by ensuring accuracy and completeness
• Document your reasoning process for audit purposes

EXTRACTION PRINCIPLES:
1. ACCURACY OVER COMPLETENESS: Only extract information that is explicitly mentioned or can be reasonably inferred from context
2. NO FABRICATION: Use null for missing fields - never invent or assume data not present in the transcript
3. NUMERICAL PRECISION: Preserve exact figures mentioned (e.g., "around £50,000" should be noted as approximate)
4. DATE HANDLING: Extract dates in mentioned format; convert to standard format when clear
5. REGULATORY AWARENESS: Flag any compliance-relevant information (e.g., vulnerable client indicators, capacity concerns)

SECTION-SPECIFIC GUIDANCE:

PERSONAL DETAILS:
• Extract full names, titles, dates of birth, marital status, and contact information
• Note any special circumstances (power of attorney, capacity issues)

EMPLOYMENT:
• Capture current and recent employment details
• Include job titles, employers, employment status, and start dates
• Note any planned changes (retirement, career transitions)

ADDRESSES:
• Current address with full details including postcode
• Previous addresses if mentioned (especially if recent moves affect financial planning)

DEPENDANTS:
• Children, elderly parents, or others financially dependent
• Include ages and any special needs or circumstances

INCOME & EXPENSES:
• Distinguish between gross and net figures
• Capture frequency (annual, monthly, weekly)
• Note sources of income and categories of expenses
• Include any planned changes or seasonal variations

PENSIONS & ASSETS:
• Current values, contribution rates, and provider details
• Include both defined benefit and defined contribution schemes
• Note any pending transfers or changes

HEALTH:
• Only extract information voluntarily disclosed that affects financial planning
• Note any critical illness cover or health-related financial concerns

OBJECTIVES:
• Primary and secondary financial goals
• Timescales and priority rankings
• Risk tolerance and capacity indicators

STEP-BY-STEP PROCESS:
For each major section, provide:
1. What information was found in the transcript
2. How you interpreted or categorized this information
3. Any assumptions made or data transformations applied
4. What information is missing but would typically be required

OUTPUT REQUIREMENTS:
• Return valid JSON matching the FinalAnswer schema exactly
• Include detailed reasoning in the 'steps' array
• Use null for genuinely missing information
• Ensure numerical values are properly typed (numbers vs strings)
• Maintain consistency in naming conventions and formatting

QUALITY CHECKS:
Before finalizing, verify:
• All extracted data can be traced back to specific transcript content
• JSON structure validates against the provided schema
• No prohibited assumptions or fabrications are present
• All reasoning steps are clearly documented
• Regulatory compliance requirements are met

Remember: Your output will be used for regulatory documentation and client advice. Accuracy and traceability are paramount.
"""


def find_facts(transcript: str) -> FactFind:
    """Returns a FinalAnswer object containing the fact-find data and the steps taken to extract it."""
    client = OpenAI()
    response = client.responses.parse(
        model="gpt-4.1",
        input=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": transcript},
        ],
        temperature=0.1,
        text_format=FactFind,
    )
    return response.output_parsed


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("transcript", type=str, help="Path to the transcript file")
    args = parser.parse_args()

    with open(args.transcript, "r") as f:
        transcript = f.read()

    result = find_facts(transcript)
    print(result.model_dump_json(indent=2, exclude_none=True))
