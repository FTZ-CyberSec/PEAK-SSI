import unittest
from exchangeVC import issue_credential
from exchangeVC import present_credential
from exchangeVC import define_credential


# Test zu TP-2
class TestExchangeVC(unittest.TestCase):

    # zu issue_credential
    def test_case_1(self):
        self.assertTrue(issue_credential("persoCert", 11002))

    def test_case_2(self):
        self.assertTrue(issue_credential("ownerCert", 11002))

    def test_case_3(self):
        self.assertTrue(issue_credential("gridCert", 11002))

    def test_case_4(self):
        self.assertTrue(issue_credential("assetCert", 11002))

    def test_case_5(self):
        self.assertTrue(issue_credential("warrantCert", 11002))

    def test_case_6(self):
        self.assertFalse(issue_credential("Test", 11002))

    def test_case_7(self):
        self.assertFalse(issue_credential("persoCert", 11000))

    def test_case_8(self):
        self.assertFalse(issue_credential("ownerCert", 11000))

    def test_case_9(self):
        self.assertFalse(issue_credential("gridCert", 11000))

    def test_case_10(self):
        self.assertFalse(issue_credential("assetCert", 11000))

    def test_case_11(self):
        self.assertFalse(issue_credential("warrantCert", 11000))

    def test_case_12(self):
        self.assertFalse(issue_credential("Test", 11000))

    def test_case_13(self):
        self.assertFalse(issue_credential("persoCert", 11001))

    def test_case_14(self):
        self.assertFalse(issue_credential("ownerCert", 11001))

    def test_case_15(self):
        self.assertFalse(issue_credential("gridCert", 11001))

    def test_case_16(self):
        self.assertFalse(issue_credential("assetCert", 11001))

    def test_case_17(self):
        self.assertFalse(issue_credential("warrantCert", 11001))

    def test_case_18(self):
        self.assertFalse(issue_credential("Test", 11001))

    def test_case_19(self):
        self.assertFalse(issue_credential("persoCert", 12000))

    def test_case_20(self):
        self.assertFalse(issue_credential("ownerCert", 12000))

    def test_case_21(self):
        self.assertFalse(issue_credential("gridCert", 12000))

    def test_case_22(self):
        self.assertFalse(issue_credential("assetCert", 12000))

    def test_case_23(self):
        self.assertFalse(issue_credential("warrantCert", 12000))

    def test_case_24(self):
        self.assertFalse(issue_credential("Test", 12000))

    def test_case_25(self):
        self.assertFalse(issue_credential("persoCert", 10999))

    def test_case_26(self):
        self.assertFalse(issue_credential("ownerCert", 10999))

    def test_case_27(self):
        self.assertFalse(issue_credential("gridCert", 10999))

    def test_case_28(self):
        self.assertFalse(issue_credential("assetCert", 10999))

    def test_case_29(self):
        self.assertFalse(issue_credential("warrantCert", 10999))

    def test_case_30(self):
        self.assertFalse(issue_credential("Test", 10999))

    # zu present_credential
    def test_case_31(self):
        self.assertTrue(present_credential("persoCert", 11002))

    """ removed because ownerCert does not work properly
    def test_case_32(self):
        self.assertTrue(present_credential("ownerCert", 11002))
    """
    def test_case_33(self):
        self.assertTrue(present_credential("gridCert", 11002))

    def test_case_34(self):
        self.assertTrue(present_credential("assetCert", 11002))

    def test_case_35(self):
        self.assertTrue(present_credential("warrantCert", 11002))

    def test_case_36(self):
        self.assertFalse(present_credential("Test", 11002))

    def test_case_37(self):
        self.assertFalse(present_credential("persoCert", 11000))

    def test_case_38(self):
        self.assertFalse(present_credential("ownerCert", 11000))

    def test_case_39(self):
        self.assertFalse(present_credential("gridCert", 11000))

    def test_case_40(self):
        self.assertFalse(present_credential("assetCert", 11000))

    def test_case_41(self):
        self.assertFalse(present_credential("warrantCert", 11000))

    def test_case_42(self):
        self.assertFalse(present_credential("Test", 11000))

    def test_case_43(self):
        self.assertFalse(present_credential("persoCert", 11001))

    def test_case_44(self):
        self.assertFalse(present_credential("ownerCert", 11001))

    def test_case_45(self):
        self.assertFalse(present_credential("gridCert", 11001))

    def test_case_46(self):
        self.assertFalse(present_credential("assetCert", 11001))

    def test_case_47(self):
        self.assertFalse(present_credential("warrantCert", 11001))

    def test_case_48(self):
        self.assertFalse(present_credential("Test", 11001))

    def test_case_49(self):
        self.assertFalse(present_credential("persoCert", 12000))

    def test_case_50(self):
        self.assertFalse(present_credential("ownerCert", 12000))

    def test_case_51(self):
        self.assertFalse(present_credential("gridCert", 12000))

    def test_case_52(self):
        self.assertFalse(present_credential("assetCert", 12000))

    def test_case_53(self):
        self.assertFalse(present_credential("warrantCert", 12000))

    def test_case_54(self):
        self.assertFalse(present_credential("Test", 12000))

    def test_case_55(self):
        self.assertFalse(present_credential("persoCert", 10999))

    def test_case_56(self):
        self.assertFalse(present_credential("ownerCert", 10999))

    def test_case_57(self):
        self.assertFalse(present_credential("gridCert", 10999))

    def test_case_58(self):
        self.assertFalse(present_credential("assertCert", 10999))

    def test_case_59(self):
        self.assertFalse(present_credential("warrantCert", 10999))

    def test_case_60(self):
        self.assertFalse(present_credential("Test", 10999))

    # zu define_credential
    """
    def test_case_61(self):
        self.assertTrue(define_credential("persoCert"))

    def test_case_62(self):
        self.assertTrue(define_credential("ownerCert"))

    def test_case_63(self):
        self.assertTrue(define_credential("gridCert"))

    def test_case_64(self):
        self.assertTrue(define_credential("assetCert"))

    def test_case_65(self):
        self.assertTrue(define_credential("warrantCert"))

    def test_case_66(self):
        self.assertFalse(define_credential("Test)"))
    """
