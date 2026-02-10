class LoanApprovalProcess:
    def approve_loan(self, applicant, amount):
        if not self.check_credit_score(applicant):
            return "Rejected: Low credit score"
        if not self.verify_income(applicant, amount):
            return "Rejected: Insufficient income"
        if not self.assess_risk(applicant, amount):
            return "Rejected: High risk"
        self.finalize_approval(applicant, amount)
        return "Approved!"
    
    def check_credit_score(self, applicant):
        pass

    def verify_income(self, applicant, amount):
        pass

    def assess_risk(self, applicant, amount):
        pass

    def finalize_approval(self, applicant, amount):
        pass

class PersonalLoanApproval(LoanApprovalProcess):
    def check_credit_score(self, applicant):
        print("[PERSONAL] Checking credit...")
        if applicant['score'] >= 650:
            return True
        else:
            return False
        
    def verify_income(self, applicant, amount):
        print("[PERSONAL] Verifying income...")
        if applicant['income'] >= amount * 3:
            return True
        else:
            return False
        
    def assess_risk(self, applicant, amount):
        print("[PERSONAL] Low risk")
        return True
    
    def finalize_approval(self, applicant, amount):
        print(f"[PERSONAL] Loan approved: ${amount}")

class MortgageLoanApproval(LoanApprovalProcess):
    def check_credit_score(self, applicant):
        print("[MORTGAGE] Checking credit...")
        if applicant['score'] >= 700:
            return True
        else:
            return False
    
    def verify_income(self, applicant, amount):
        print("[MORTGAGE] Verifying income...")
        if applicant['income'] >= amount * 4:
            return True
        else:
            return False
        
    def assess_risk(self, applicant, amount):
        print("[MORTGAGE] Checking collateral...")
        return True
    
    def finalize_approval(self, applicant, amount):
        print(f"[MORTGAGE] Mortgage approved: ${amount}")

applicant = {
    'name': 'John',
    'score': 720,
    'income': 80000
}

personal = PersonalLoanApproval()
print(personal.approve_loan(applicant, 20000))

mortgage = MortgageLoanApproval()
print(mortgage.approve_loan(applicant, 150000))

