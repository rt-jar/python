import re


def extract_case_info(text):
    magistrate_judge = None
    circuit_judges = None
    try:
        # Define regular expressions for each piece of information
        case_no_pattern = re.compile(r'No.\s(\d+-\d+)')
        magistrate_judge_pattern = re.compile(r'Judge:\s([A-Z][\w\s.]+)____', re.IGNORECASE)        
        circuit_judges_pattern = re.compile(r'Before:([A-Za-z,\s]+), Circuit Judges', re.IGNORECASE)
        opinion_filed_date_pattern = re.compile(r'([\w\s.]+)filed:\s([A-Z][a-z]+\s\d{1,2},\s\d{4})', re.IGNORECASE)

        # Extract information using regular expressions
        case_no = re.search(case_no_pattern, text).group(1)
        magistrate_judge = re.search(magistrate_judge_pattern, text).group(1).replace("_", "")
        circuit_judges_match = re.search(circuit_judges_pattern, text)
        circuit_judges = circuit_judges_match.group(1).strip() if circuit_judges_match else None
        opinion_filed_date = re.search(opinion_filed_date_pattern, text).group(1)
    except Exception as e:
        print(e)
    
    return {
        'Case Number': case_no,
        'Judge': magistrate_judge if magistrate_judge else None,
        'Circuit Judges': circuit_judges,
        'Opinion Filed Date': opinion_filed_date
    }

# Example usage with the provided text
text = """
UNITED STATES COURT OF APPEALS FOR THE THIRD CIRCUIT ________________
Nos. 22-2003, 22-2004, 22-2005, 22-2006, 22-0007, 22-2008, 22-2009, 22-2010, 22-2011 ________________
In re: LTL MANAGEMENT, LLC Debtor
LTL MANAGEMENT, LLC v.
THOSE PARTIES LISTED ON APPENDIX A TO COMPLAINT
AND JOHN AND JANE DOES 1-1000
*OFFICIAL COMMITTEE OF TALC CLAIMANTS, Appellant in case Nos. 22-2003, 22-2004 and 22-2005
*OFFICIAL COMMITTEE OF TALC CLAIMANTS; PATRICIA COOK;
EVAN PLOTKIN; RANDY DEROUEN; KRISTIE DOYLE, as estate representative of Dan Doyle; KATHERINE TOLLEFSON;
TONYA WHETSEL, as estate representative of Brandon Wetsel;
GIOVANNI SOSA; JAN DEBORAH MICHELSON- BOYLE,
  
Appellants in case Nos. 22-2006, 22-2007 and 22-2008
ARNOLD & ITKIN LLP, on behalf of certain personal injury claimants represented by Arnold & Itkin,
Appellant in case No. 22-2009
AYLSTOCK WITKIN KREIS & OVERHOLTZ PLLC, on behalf of more
than three thousand holders of talc claims,
Appellant in case Nos. 22-2010 and 22-2011 *(Amended per Court’s Order dated 06/10/2022)
Appeal from the United States Bankruptcy Court for the District of New Jersey
(District Court No.: 21-bk-30589; 21-ap-03032) Bankruptcy Judge: Honorable Michael B. Kaplan
Argued September 19, 2022
Before AMBRO, RESTREPO, and FUENTES, Circuit Judges
(Opinion filed: January 30, 2023)
"""

case_info = extract_case_info(text)

# Print the extracted information
for key, value in case_info.items():
    print(f'{key}: {value}')
