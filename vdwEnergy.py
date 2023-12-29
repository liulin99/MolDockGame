#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#https://github.com/csimmerling/ff19SB_201907/blob/master/forcefield_files/parm19.dat
#based on ff19SB
ff18SB={
  "H":(0.6000,0.0157),  "HO":(0.0000,0.0000),  "HS":(0.6000,0.0157),  "HC":(1.4870,0.0157),  "H1":(1.3870,0.0157),
  "H2":(1.2870,0.0157),  "H3":(1.1870,0.0157),  "HP":(1.1000,0.0157),  "HA":(1.4590,0.0150),  "H4":(1.4090,0.0150),
  "H5":(1.3590,0.0150),  "HW":(0.0000,0.0000),  "HZ":(1.4590,0.0150),
  "O":(1.6612,0.2100),  "O2":(1.6612,0.2100),  "OW":(1.7683,0.1520),  "OH":(1.7210,0.2104),  "OS":(1.6837,0.1700),
  "OP":(1.8500,0.1700),  "IP":(1.8680,0.00277),
  "C*":(1.9080,0.0860),  "CI":(1.9080,0.1094),  "C5":(1.9080,0.0860),  "C4":(1.9080,0.0860),  "CT":(1.9080,0.1094),
  "C":(1.9080,0.0860),  "CC":(1.9080,0.0860),  "CA":(1.9080,0.0860),  "CV":(1.9080,0.0860), "CR":(1.9080,0.0860),  "CW":(1.9080,0.0860)
    , "CM":(1.9080,0.086),"CN":(1.9080,0.086),"Cs":(3.3950,0.0000806),  "CB":(1.9080,0.0860),
  "N":(1.8240,0.1700), "NB":(1.8240,0.1700),  "NA":(1.8240,0.1700),  "N3":(1.8240,0.1700),  "N2":(1.8240,0.1700),  "S":(2.0000,0.2500),"SH":(2.0000,0.2500),"C0":(1.7131,0.459789),
  "SH":(2.0000,0.2500),  "P":(2.1000,0.2000),  "MG":(0.7926,0.8947),  "Zn":(1.10,0.0125),
  "F":(1.75,0.061),  "Cl":(1.948,0.265),  "Br":(2.22,0.320),  "I":(2.35,0.40),  "EP":(0.00,0.0000) ,"K":(2.6580,0.000328),
  "Li":(1.1370,0.0183),"Rb":(2.9560,0.00017)}


# In[ ]:


atom2vdwatom={
("ILE","N"):"N", ("ILE","CA"):"CT",("ILE","CB"):"CT",("ILE","CG1"):"CT",("ILE","CG2"):"CT",
("ILE","CD1"):"CT",("ILE","C"):"C",("ILE","O"):"O",("ILE","OXT"):"OH",("ILE","HXT"):"HO",
("ILE","H2"):"H",("ILE","H"):"H",("ILE","HA"):"H1",("ILE","HB"):"HC",("ILE","HG12"):"HC",
("ILE","HG13"):"HC",("ILE","HG21"):"HC",("ILE","HG22"):"HC",("ILE","HG23"):"HC",("ILE","HD11"):"HC",
("ILE","HD12"):"HC",("ILE","HD13"):"HC",("PHE","N"):"N", ("PHE","H2"):"H",("PHE","H"):"H",
("PHE","HA"):"H1", ("PHE","C"):"C",("PHE","OXT"):"OH", ("PHE","HXT"):"HO", ("PHE","CA"):"CT",
("PHE","CB"):"CT", ("PHE","CG"):"CA",("PHE","CD1"):"CA", ("PHE","CD2"):"CA", ("PHE","CE1"):"CA",
("PHE","CE2"):"CA",("PHE","CZ"):"CA",("PHE","O"):"O",("PHE","HB2"):"HC",("PHE","HB3"):"HC",("PHE","HD1"):"HA",
("PHE","HD2"):"HA",("PHE","HE1"):"HA", ("PHE","HE2"):"HA",("PHE","HZ"):"HA", ("VAL","N"):"N",("VAL","H2"):"H",
("VAL","H"):"H",("VAL","H1"):"H",("VAL","H3"):"H",("VAL","C"):"C",("VAL","O"):"O",("VAL","OXT"):"OH",("VAL","HXT"):"HO",("VAL","HA"):"H1",
("VAL","HB"):"HC",("VAL","HG11"):"HC",("VAL","HG12"):"HC",("VAL","HG13"):"HC",
("VAL","HG21"):"HC",("VAL","HG22"):"HC",("VAL","HG23"):"HC",("VAL","CA"):"CT",("VAL","CB"):"CT",
("VAL","CG1"):"CT",("VAL","CG2"):"CT",("LEU","N"):"N",("LEU","H"):"H",("LEU","C"):"C",("LEU","O"):"O",
("LEU","H2"):"H",("LEU","H1"):"H",("LEU","H3"):"H",("LEU","HA"):"H1",("LEU","OXT"):"OH",("LEU","HXT"):"HO",("LEU","CD2"):"CT",("LEU","CD1"):"CT",
("LEU","CA"):"CT",("LEU","CB"):"CT",("LEU","CG"):"CT",("LEU","HB2"):"HC",("LEU","HB3"):"HC",
("LEU","HG"):"HC",("LEU","HD12"):"HC",("LEU","HD11"):"HC",("LEU","HD13"):"HC",("LEU","HD22"):"HC",("LEU","HD21"):"HC",("LEU","HD23"):"HC",("TRP","N"):"N",("TRP","H2"):'H', ("TRP","HE1"):'H',  ("TRP","H"):'H',
("TRP","C"):"C",("TRP","O"):"O", ("TRP","HA"):"H1", ("TRP","OXT"):"OH", ("TRP","HXT"):"HO", ("TRP","NE1"):"NA",
("TRP","CB"):"CT",("TRP","CA"):"CT",("TRP","CG"):"C*",("TRP","CD1"):"CW",("TRP","CD2"):"CB",
("TRP","CE2"):"CN",("TRP","HD1"):"H4",("TRP","CH2"):"CA",("TRP","CE3"):"CA",("TRP","CZ2"):"CA",
("TRP","CZ3"):"CA",("TRP","HZ3"):"HA",("TRP","HZ2"):"HA",("TRP","HH2"):"HA",("TRP","HE3"):"HA",
("TRP","HB3"):"HC",("TRP","HB2"):"HC",("MET","N"):"N",("MET","H"):"H",("MET","H1"):"H",("MET","H3"):"H",("MET","H2"):"H",("MET","C"):"C",("MET","O"):"O",
("MET","HA"):"H1",("MET","OXT"):"OH",("MET","HXT"):"HO", ("MET","CE"):"CT",  ("MET","CA"):"CT",
("MET","CB"):"CT",("MET","CG"):"CT",("MET","SD"):"S", ("MET","HE3"):"H1",  ("MET","HG2"):"H1",
("MET","HG3"):"H1",("MET","HE1"):"H1",("MET","HE2"):"H1",("MET","HB3"):"HC",("MET","HB2"):"HC",
("ALA","N"):"N", ("ALA","H"):"H",  ("ALA","H2"):"H",("ALA","H1"):"H",("ALA","H3"):"H",("ALA","C"):"C",  ("ALA","O"):"O",
("ALA","HA"):"H1",("ALA","OXT"):"OH",  ("ALA","HXT"):"HO", ("ALA","CA"):"CT", ("ALA","CB"):"CT",
("ALA","HB3"):"HC",("ALA","HB1"):"HC", ("ALA","HB2"):"HC",("GLY","N"):"N", ("GLY","H"):"H",
("GLY","H2"):"H",("GLY","H1"):"H",("GLY","H3"):"H",("GLY","C"):"C",("GLY","O"):"O",("GLY","OXT"):"OH",("GLY","HXT"):"HO", ("GLY","HA3"):"H1",
("GLY","HA2"):"H1",("GLY","CA"):"CT",("CYS", "N"):"N", ("CYS", "H2"):"H", ("CYS", "H"):"H", ("CYS","C"):"C",
("CYS","O"):"O",("CYS","OXT"):"OH",("CYS","HXT"):"HO",("CYS","CA"):"CT", ("CYS","CB"):"CT",("CYS","SG"):"SH",
("CYS","HB3"):"H1",("CYS","HA"):"H1", ("CYS","HB2"):"H1",("CYS","HG"):"HS",("TYR","N"):"N", ("TYR","H"):"H",
("TYR","H2"):"H", ("TYR","H1"):"H",("TYR","H3"):"H",("TYR","C"):"C", ("TYR","CZ"):"C",("TYR","O"):"O",("TYR","OXT"):"OH",("TYR","HXT"):"HO",
("TYR","CA"):"CT", ("TYR","CB"):"CT",("TYR","CG"):"CA",("TYR","CD1"):"CA",("TYR","CD2"):"CA",("TYR","CE1"):"CA",
("TYR","CE2"):"CA",("TYR","HD1"):"HA",("TYR","HD2"):"HA",("TYR","HE1"):"HA", ("TYR","HE2"):"HA",("TYR","OH"):"OH",
("TYR","HH"):"HO",("TYR","HA"):"H1", ("TYR","HB2"):"HC", ("TYR","HB3"):"HC",("PRO","N"):"N",("PRO","C"):"C",
("PRO","O"):"O",("PRO","H"):"H",("PRO","OXT"):"OH",("PRO","HXT"):"HO", ("PRO","CA"):"CT",("PRO","CD"):"CT",
("PRO","CB"):"CT",("PRO","CG"):"CT",("PRO","HA"):"H1",("PRO","HD2"):"H1", ("PRO","HD3"):"H1",("PRO","HG3"):"HC",
("PRO","HB2"):"HC",("PRO","HB3"):"HC",("PRO","HG2"):"HC",("THR","N"):"N",("THR","C"):"C",("THR","O"):"O",
("THR","OXT"):"OH",("THR","HXT"):"HO",("THR","CG2"):"CT",("THR","CA"):"CT",("THR","CB"):"CT",("THR","OG1"):"OH",
("THR","H2"):"H", ("THR","H3"):"H", ("THR","H"):"H", ("THR","H1"):"H", ("THR","HA"):"H1", ("THR","HB"):"H1",("THR","HG1"):"HO", ("THR","HG23"):"HC",
("THR","HG22"):"HC",("THR","HG21"):"HC",("SER","N"):"N",("SER","C"):"C",("SER","O"):"O", ("SER","H"):"H",
("SER","H2"):"H",("SER","H1"):"H",("SER","H3"):"H",("SER","OXT"):"OH", ("SER","HXT"):"HO", ("SER","CA"):"CT", ("SER","CB"):"CT",("SER","OG"):"OH",
("SER","HB3",):"H1",("SER","HA",):"H1",("SER","HB2",):"H1",("SER","HG"):"HO",

    ("HIS","N"):"N",("HIS","C"):"C",
("HIS","O"):"O", ("HIS","H"):"H",("HIS","H1"):"H",("HIS","H3"):"H",("HIS","H2"):"H",("HIS","HE2"):"H",("HIS","HD1"):"H",("HIS","OXT"):"OH",
("HIS","HXT"):"HO",("HIS","ND1"):"NA",("HIS","NE2"):"NA", ("HIS","CA"):"CT", ("HIS","CB"):"CT",("HIS","CG"):"CC",
("HIS","CD2"):"CW",("HIS","CE1"):"CR",("HIS","HA"):"H1", ("HIS","HB2"):"HC", ("HIS","HB3"):"HC",("HIS","HD2"):"H4",
("HIS","HE1"):"H5",
    
    ("GLU","N"):"N", ("GLU","C"):"C", ("GLU","CD"):"C",("GLU","O"):"O", ("GLU","H2"):"H",
("GLU","H"):"H",("GLU","H1"):"H",("GLU","H3"):"H",("GLU","OXT"):"OH", ("GLU","HE2"):"HO",("GLU","HXT"):"HO", ("GLU","CG"):"CT",
("GLU","CA"):"CT",("GLU","CB"):"CT", ("GLU","OE1"):"O2",("GLU","OE2"):"O2",("GLU","HA"):"H1",
("GLU","HG3"):"HC", ("GLU","HB2"):"HC",("GLU","HB3"):"HC",("GLU","HG2"):"HC",("ASN","N"):"N",
("ASN","ND2"):"N", ("ASN","C",):"C", ("ASN","CG",):"C", ("ASN","O"):"O",
("ASN","OD1"):"O",("ASN","H"):"H",("ASN","H1"):"H",("ASN","H3"):"H",("ASN","HD22"):"H",("ASN","HD21"):"H",("ASN","H2"):"H",
("ASN","OXT"):"OH",("ASN","HXT"):"HO", ("ASN","CA"):"CT", ("ASN","CB"):"CT",("ASN","HA"):"H1",
("ASN","HB2"):"HC", ("ASN","HB3"):"HC", ("GLN","N"):"N", ("GLN","NE2"):"N", ("GLN","C"):"C", ("GLN","CD"):"C", ("GLN","O"):"O",
("GLN","OE1"):"O",("GLN","HE22"):"H",("GLN","HE21"):"H",("GLN","H"):"H",("GLN","H1"):"H",("GLN","H3"):"H",("GLN","H2"):"H",
("GLN","OXT"):"OH",("GLN","HXT"):"HO", ("GLN","CG"):"CT",("GLN","CA"):"CT",("GLN","CB"):"CT",
("GLN","HA"):"H1",("GLN","HG3"):"HC",("GLN","HB2"):"HC",("GLN","HB3"):"HC",("GLN","HG2"):"HC",("ASP","N"):"N",
("ASP","C"):"C", ("ASP","CG"):"C", ("ASP","OD1"):"O2", ("ASP","OD2"):"O2",
("ASP","O"):"O", ("ASP","H2"):"H", ("ASP","H"):"H", ("ASP","OXT"):"OH", ("ASP","HXT"):"HO", ("ASP","CA"):"CT",
("ASP","CB"):"CT",("ASP","HA"):"H1", ("ASP","HB2"):"HC", ("ASP","HB3"):"HC",("ASP","HD2"):"HO",
("LYS","N"):"N",("LYS","C"):"C", ("LYS","CE"):"CT",  ("LYS","CA"):"CT",   ("LYS","CB"):"CT",
("LYS","CG"):"CT",("LYS","CD"):"CT",("LYS","O"):"O",("LYS","NZ"):"N3",("LYS","OXT"):"OH",
("LYS","HXT"):"HO", ("LYS","H2"):"H",("LYS","H1"):"H",("LYS","H3"):"H", ("LYS","H"):"H",("LYS","HA"):"H1", ("LYS","HD3"):"HC",
("LYS","HB2"):"HC", ("LYS","HB3"):"HC", ("LYS","HG2"):"HC", ("LYS","HG3"):"HC", ("LYS","HD2"):"HC",
("LYS","HE2"):"HP", ("LYS","HE3"):"HP", ("LYS","HZ3"):"H",("LYS","HZ2"):"H",("LYS","HZ1"):"H",("ARG","N"):"N",
("ARG","C"):"C",("ARG","O"):"O",("ARG","OXT"):"OH",("ARG","HXT"):"HO", ("ARG","H"):"H",  ("ARG","H2"):"H",
("ARG","HH11"):"H",("ARG","HH12"):"H",("ARG","HH21"):"H",
("ARG","HH22"):"H",("ARG","HE"):"H", ("ARG","HD3"):"H1",  ("ARG","HA"):"H1",   ("ARG","HD2"):"H1",
 ("ARG","NH2"):"N2",  ("ARG","NE"):"N2",   ("ARG","NH1"):"N2",("ARG","CG"):"CT",("ARG","CA"):"CT",
("ARG","CD"):"CT",("ARG","CB"):"CT",("ARG","CZ"):"CA", ("ARG","HG3"):"HC",  ("ARG","HG2"):"HC",
   ("ARG","HB3"):"HC",    ("ARG","HB2"):"HC",("PCA","N"):"N",("PCA","CD"):"CC",("PCA","C"):"C", ("PCA","O"):"O", ("PCA","OE"):"O",
 ("PCA","CG"):"CT",  ("PCA","CA"):"CT",   ("PCA","CB"):"CT",("PCA","H"):"H",("PCA","OXT"):"OH",
("PCA","HXT"):"HO",("PCA","HA"):"H1", ("PCA","HG3"):"HC",  ("PCA","HG2"):"HC",   ("PCA","HB3"):"HC",
    ("PCA","HB2"):"HC",("SEP","N"):"N",("SEP","C"):"C",("SEP","O"):"O",("SEP","HA"):"H1", ("SEP","CA"):"CT",
 ("SEP","CB"):"CT",("SEP","P"):"P",("SEP","O1P"):"O2", ("SEP","OG"):"OH",  ("SEP","O2P"):"OH",   ("SEP","O3P"):"OH",    ("SEP","OXT"):"OH",
 ("SEP","HXT"):"HO", ("SEP","HOP2"):"HO", ("SEP","HOP3"):"HO", ("SEP","H2"):"H", ("SEP","H"):"H",("SEP","HB3"):"H1",
("SEP","HB2"):"H1",("TPO","N"):"N", ("TPO","CA"):"CT",  ("TPO","CB"):"CT",   ("TPO","CG2"):"CT",  ("TPO","C"):"C",
 ("TPO","HA"):"H1", ("TPO","HB"):"H1", ("TPO","O"):"O",  ("TPO","O1P"):"O",
("TPO","OXT"):"OH",("TPO","O2P"):"OH",("TPO","O3P"):"OH",("TPO","OG1"):"OH",("TPO","P"):"P",
 ("TPO","H"):"H", ("TPO","H2"):"H", ("TPO","HG21"):"HC",  ("TPO","HG22"):"HC", ("TPO","HG23"):"HC",
 ("TPO","HXT"):"HO", ("TPO","HOP2"):"HO",  ("TPO","HOP3"):"HO",("M0H","N"):"N", ("M0H","CA"):"CT",  ("M0H","CB"):"CT",   ("M0H","CD"):"CT",("M0H","C"):"C",
 ("M0H","HD2"):"H1",  ("M0H","HA"):"H1",   ("M0H","HB2"):"H1",    ("M0H","HB1"):"H1",      ("M0H","HD1"):"H1",
("M0H","O"):"OH",("M0H","OXT"):"O",("M0H","OE"):"OH",("M0H","SG"):"S", ("M0H","HO"):"HO",
  ("M0H","HE"):"HO", ("M0H","HN1"):"H", ("M0H","HN2"):"H",("CSX","N"):"N",("CSX","C"):"C", ("CSX","CA"):"CT", ("CSX","CB"):"CT",("CSX","O"):"O",("CSX","OD"):"O2",
("CSX","OXT"):"OH",("CSX","SG"):"S", ("CSX","H2"):"H",  ("CSX","HG"):"H",   ("CSX","H"):"H", ("CSX","HB3"):"H1",
  ("CSX","HA"):"H1",   ("CSX","HB2"):"H1", ("CSX","HXT"):"HO",("ORN","N"):"N",("ORN","NE"):"N3", ("ORN","CG"):"CT",  ("ORN","CA"):"CT",   ("ORN","C"):"CT",
    ("ORN","CD"):"CT",      ("ORN","CB"):"CT",("ORN","O"):"O",("ORN","OXT"):"OH", ("ORN","HE2"):"H",
  ("ORN","H"):"H",   ("ORN","H2"):"H",    ("ORN","HE1"):"H",("ORN","HA"):"H1", ("ORN","HG3"):"HC",
  ("ORN","HB2"):"HC",   ("ORN","HB3"):"HC",    ("ORN","HG2"):"HC", ("ORN","HD2"):"HP", ("ORN","HD3"):"HP",
("ORN","HXT"):"HO",("MLY","N"):"N",("MLY","NZ"):"N3",("MLY","O"):"O",("MLY","OXT"):"OH",("MLY","C"):"C",
 ("MLY","CH2"):"CT",  ("MLY","CA"):"CT",   ("MLY","CD"):"CT",    ("MLY","CB"):"CT",
     ("MLY","CG"):"CT",      ("MLY","CE"):"CT",       ("MLY","CH1"):"CT", ("MLY","H"):"H", ("MLY","H2"):"H",
("MLY","HA"):"H1", ("MLY","HD3"):"HC",  ("MLY","HB2"):"HC",   ("MLY","HB3"):"HC",
    ("MLY","HG2"):"HC",     ("MLY","HG3"):"HC",      ("MLY","HD2"):"HC", ("MLY","HH23"):"HP",
  ("MLY","HE2"):"HP",   ("MLY","HE3"):"HP",    ("MLY","HH11"):"HP",     ("MLY","HH12"):"HP",      ("MLY","HH13"):"HP",
       ("MLY","HH21"):"HP",        ("MLY","HH22"):"HP",("MLY","HXT"):"HO",("DM0","N"):"N",("DM0","NZ"):"N3", ("DM0","CA"):"CT",  ("DM0","CD"):"CT",   ("DM0","CB"):"CT",
    ("DM0","CG"):"CT",     ("DM0","CE"):"CT",      ("DM0","CH1"):"CT",       ("DM0","CH2"):"CT",        ("DM0","CM1"):"CT",
         ("DM0","CM2"):"CT",("DM0","C"):"C",("DM0","O"):"O",("DM0","OXT"):"OH",("DM0","HA"):"H1",
 ("DM0","HDA"):"HC",  ("DM0","HB"):"HC",   ("DM0","HBA"):"HC",    ("DM0","HG"):"HC",     ("DM0","HGA"):"HC",
      ("DM0","HD"):"HC",("DM0","HXT"):"HO", ("DM0","HH2B"):"HP",  ("DM0","HE"):"HP",   ("DM0","HEA"):"HP",
    ("DM0","HM2"):"HP",     ("DM0","HM2A"):"HP",      ("DM0","HM2B"):"HP",       ("DM0","HM1"):"HP",        ("DM0","HM1A"):"HP",
         ("DM0","HM1B"):"HP",          ("DM0","HH1"):"HP",           ("DM0","HH1A"):"HP",            ("DM0","HH1B"):"HP",
             ("DM0","HH2"):"HP",              ("DM0","HH2A"):"HP",("CSO","N"):"N",("CSO","C"):"C", ("CSO","HA"):"H1",  ("CSO","HB2"):"H1",   ("CSO","HB3"):"H1",
 ("CSO","CB"):"CT",  ("CSO","CA"):"CT",("CSO","O"):"O", ("CSO","OD"):"OH",  ("CSO","OXT"):"OH",
("CSO","SG"):"S", ("CSO","HN2"):"H",  ("CSO","H"):"H", ("CSO","HD"):"HO", ("CSO","HXT"):"HO",("MLZ","N"):"N",("MLZ","NZ"):"N3", ("MLZ","CA"):"CT",  ("MLZ","CM"):"CT",   ("MLZ","CD"):"CT",
    ("MLZ","CB"):"CT",     ("MLZ","CG"):"CT",      ("MLZ","CE"):"CT",
("MLZ","C"):"C",("MLZ","O"):"O",("MLZ","OXT"):"OH",("MLZ","H2"):"H",("MLZ","HZ"):"H",
("MLZ","H"):"H",("MLZ","HA"):"H1", ("MLZ","HE3"):"HC", ("MLZ","HB2"):"HC", ("MLZ","HB3"):"HC",
 ("MLZ","HG2"):"HC", ("MLZ","HG3"):"HC", ("MLZ","HD2"):"HC", ("MLZ","HD3"):"HC",
 ("MLZ","HE2"):"HC",("MLZ","HXT"):"HO", ("MLZ","HCM3"):"HP",("MLZ","HCM2"):"HP",("MLZ","HCM1"):"HP",("MSE","C"):"C", ("MSE","CE"):"CT",("MSE","N"):"N",  ("MSE","CA"):"CT", ("MSE","CB"):"CT", ("MSE","CG"):"CT",
("MSE","O"):"O",("MSE","OXT"):"OH",("MSE","SE"):"S",("MSE","H"):"H", ("MSE","HN2"):"H",
("MSE","HA"):"H1",("MSE","HXT"):"HO",("MSE","HB2"):"HC", ("MSE","HB3"):"HC",
 ("MSE","HE3"):"H1",("MSE","HE1"):"H1",("MSE","HG2"):"H1",("MSE","HG3"):"H1",("MSE","HE2"):"H1",
("XCN","N"):"N",("XCN","NC"):"N3",("XCN","C"):"C", ("XCN","CA",):"CT", ("XCN","CB",):"CT",
 ("XCN","SG"):"S", ("XCN","O"):"O", ("XCN","OXT"):"OH", ("XCN","CS"):"CA", ("XCN","HN"):"H",
 ("XCN","HNX"):"H", ("XCN","HB"):"H1",  ("XCN","HBA"):"H1", ("XCN","HA"):"H1",("XCN","HXT"):"HO",
              ("OCS","N"):"N", ("OCS","CB"):"CT", ("OCS","CA"):"CT", ("OCS","C"):"C", ("OCS","OD2"):"O2",
  ("OCS","OXT"):"O2",  ("OCS","O"):"O", ("OCS","OD1"):"O2", ("OCS","OD3"):"O2", ("OCS","SG"):"S",
 ("OCS","H"):"H", ("OCS","HN2"):"H", ("OCS","HB3"):"H1",  ("OCS","HB2"):"H1",   ("OCS","HA"):"H1",('CSS',"C"):"C",('CSS',"O"):"O",('CSS',"OXT"):"O2", ('CSS',"SD"):"S",  ('CSS',"SG"):"S",
 ('CSS',"H"):"H", ('CSS',"HN2"):"H", ('CSS',"HA"):"H1",  ('CSS',"HB2"):"H1",   ('CSS',"HB3"):"H1",
('CSS',"HD"):"HS",('CSS',"HXT"):"HO", ("OCS","HXT"):"HO", ("OCS","HD2"):"HO",("XPL","N"):"N",("XPL","NZ"):"N3",("XPL","N3"):"N2",("XPL","N2"):"NA", ("XPL","O"):"O",
 ("XPL","O2"):"O",("XPL","OXT"):"OH",("XPL","C"):"C", ("XPL","CE"):"CT",  ("XPL","CB2"):"CT",
   ("XPL","C2"):"CT",    ("XPL","CA"):"CT",     ("XPL","CD"):"CT",      ("XPL","CG"):"CT",
       ("XPL","CB"):"CT",("XPL","CA2"):"CC",("XPL","CE2"):"CR", ("XPL","CG2"):"CV",
 ("XPL","CD2"):"CV",("XPL","HA"):"H1", ("XPL","HB2B"):"HC",  ("XPL","HA2"):"HC",
   ("XPL","HB"):"HC",    ("XPL","HBA"):"HC",     ("XPL","HD"):"HC",      ("XPL","HDA"):"HC",
       ("XPL","HGA"):"HC",        ("XPL","HG"):"HC",         ("XPL","HB2"):"HC",
          ("XPL","HB2A"):"HC", ("XPL","HN3A"):"H", ("XPL","HN3"):"H", ("XPL","HNA"):"H",
 ("XPL","HN"):"H", ("XPL","HNZ"):"H", ("XPL","HN2"):"H",("XPL","HXT"):"HO",
 ("XPL","HG2"):"H4",  ("XPL","HD2A"):"H4",   ("XPL","HE2"):"H4",    ("XPL","HD2"):"H4",
 ("XPL","HEA"):"HP", ("XPL","HE"):"HP",("PYL","N"):"N",("PYL","N2"):"NB",("PYL","NZ"):"N3",("PYL","O2"):"O2",("PYL","O"):"O",
("PYL","OXT"):"OH",("PYL","HXT"):"HO", ("PYL","HZ"):"H",  ("PYL","H2"):"H",
 ("PYL","H"):"H",("PYL","HA"):"H1",("PYL","CA2"):"CC",
 ("PYL","C2"):"C", ("PYL","C"):"C", ("PYL","CG"):"CT",  ("PYL","CB2"):"CT",   ("PYL","CA"):"CT",    ("PYL","CE"):"CT",     ("PYL","CD"):"CT",      ("PYL","CB"):"CT", ("PYL","CD2"):"CV", ("PYL","CG2"):"CV",
("PYL","CE2"):"CW", ("PYL","HE2"):"HP", ("PYL","HE3"):"HP", ("PYL","HG22"):"HC",  ("PYL","HD32"):"HC",   ("PYL","HD22"):"HC",
    ("PYL","HB2"):"HC",     ("PYL","HB3"):"HC",      ("PYL","HG2"):"HC",
       ("PYL","HG3"):"HC",        ("PYL","HD3"):"HC",         ("PYL","HD2"):"HC",
          ("PYL","HB22"):"HC",           ("PYL","HB12"):"HC",          ("PYL","HB32"):"HC",
("PYL","HA2"):"CA",("PYL","HE22"):"H5",("AYA","N"):"N", ("AYA","CA"):"CT",  ("AYA","CB"):"CT",  ("AYA","CM"):"CT",
 ("AYA","CT"):"C", ("AYA","C"):"C",("AYA","O",):"O",("AYA","OT"):"O2",("AYA","HM1"):"HC",("AYA","HM2"):"HC",
    ("AYA","HM3"):"HC", ("AYA","HB3"):"HC", ("AYA","HB1"):"HC", ("AYA","HB2"):"HC",
("AYA","OXT"):"OH",("AYA","H"):"H",("AYA","HA"):"H1",("AYA","HXT"):"HO",("CSS","N"):"N",("CSS","C"):"C", ("CSS","CA"):"CT", ("CSS","CB"):"CT", ("CSS","O"):"O",
 ("CSS","OXT"):"O2", ("CSS","SG"):"S", ("CSS","SD"):"S", ("CSS","H"):"H", ("CSS","HN2"):"H",
 ("CSS","HB3"):"H1",  ("CSS","HB2"):"H1",   ("CSS","HA"):"H1",("CSS","HD"):"HS",("CSS","HXT"):"HO",("CXM","N"):"N",("CXM","O"):"O2",("CXM","ON1"):"O", ("CXM","ON2"):"OH",  ("CXM","OXT"):"OH",
  ("CXM","SD"):"S", ("CXM","HE3"):"H1",  ("CXM","HE3"):"HE2",   ("CXM","HE3"):"HE1",
    ("CXM","HE3"):"HG3",     ("CXM","HE3"):"HG2", ("CXM","CN"):"CT",  ("CXM","CA"):"CT",
   ("CXM","C"):"CT",    ("CXM","CB"):"CT",     ("CXM","CG"):"CT",      ("CXM","CE"):"CT",
("CXM","H"):"H",("CXM","HA"):"H1", ("CXM","HB2"):"HC", ("CXM","HB3"):"HC",
 ("CXM","HXT"):"HO", ("CXM","HO2"):"HO", ("YCM","N"):"N", ("YCM","NZ2"):"N", ("YCM","HZ22"):"H",  ("YCM","HZ21"):"H",
   ("YCM","H2"):"H",    ("YCM","H"):"H",("YCM","SG"):"S", ("YCM","O"):"O",
 ("YCM","OZ1"):"O", ("YCM","OXT",):"OH", ("YCM","CE"):"C", ("YCM","C"):"C",
 ("YCM","CD"):"CT",  ("YCM","CB"):"CT",   ("YCM","CCAD"):"CT", ("YCM","HA"):"H1",
  ("YCM","HD3"):"H1",   ("YCM","HD2"):"H1",    ("YCM","HB3"):"H1",     ("YCM","HB2"):"H1",
("YCM","HXT"):"HO",("TOX","N"):"N",("TOX","NE1"):"NB",("TOX","C"):"C",("TOX","O"):"O", ("TOX","CA"):"CT",
 ("TOX","CB"):"CT", ("TOX","CG"):"C*", ("TOX","CD1"):"CW", ("TOX","H7"):"H4", ("TOX","CE2"):"CN",
 ("TOX","CD2"):"CB", ("TOX","CZ2"):"CA",  ("TOX","CH2"):"CA",   ("TOX","CZ3"):"CA",
    ("TOX","CE3"):"CA",("TOX","OXT"):"OH", ("TOX","O2"):"O2", ("TOX","O1"):"O2",
 ("TOX","H1"):"H", ("TOX","H2"):"H", ("TOX","H3"):"HO", ("TOX","H13"):"HO",
 ("TOX","H4"):"H1", ("TOX","H5"):"HC", ("TOX","H6"):"HC", ("TOX","H11"):"HA",
 ("TOX","H8"):"HA",  ("TOX","H9"):"HA",   ("TOX","H10"):"HA",("T8L", "N"):"N", ("T8L","CA"):"CT",  ("T8L","CB"):"CT", ("T8L","CG2"):"CT",
("T8L","C"):"C", ("T8L","H9",):"HC",  ("T8L","H8",):"HC",  ("T8L","H7",):"HC",
("T8L","H4"):"H1", ("T8L","H6"):"H1",("T8L","S1"):"S",("T8L","H1"):"H",
 ("T8L","H2"):"H", ("T8L","O"):"O", ("T8L","O1P"):"O",("T8L","H10"):"HO",
("T8L","H3"):"HO",("T8L","H11"):"HS",("T8L","P"):"P",("T8L","O1"):"OH",
 ("T8L","O2P"):"O2", ("T8L","OG1"):"O2",("SCY","N"):"N", ("SCY","H"):"H", ("SCY","H2"):"H",("SCY","O"):"O",("SCY","OCD"):"O2",
("SCY","OXT"):"OH", ("SCY","CA"):"CT",  ("SCY","CE"):"CT",   ("SCY","CD"):"CT",
    ("SCY","CB"):"CT",("SCY","C"):"C",("SCY","SG"):"S", ("SCY","HB3"):"H1",
  ("SCY","HB2"):"H1",   ("SCY","HA"):"H1", ("SCY","HE3"):"HC",  ("SCY","HE2"):"HC",   ("SCY","HE1"):"HC",
("SCY","HXT"):"HO",("PTR","N"):"N", ("PTR","H"):"H", ("PTR","HN2"):"H", ("PTR","C"):"C",
 ("PTR","CZ"):"C",("PTR","P"):"P", ("PTR","CB"):"CT",  ("PTR","CA"):"CT",
 ("PTR","CE2"):"CA",  ("PTR","CE1"):"CA",   ("PTR","CD2"):"CA",    ("PTR","CD1"):"CA",
     ("PTR","CG"):"CA",("PTR","O1P"):"O",("PTR","O"):"O",("PTR","OH"):"O2", ("PTR","OXT"):"OH",  ("PTR","O2P"):"OH",
   ("PTR","O3P"):"OH",("PTR","HA"):"H1",("PTR","HXT"):"HO", ("PTR","HD1"):"HA",  ("PTR","HE2"):"HA",
   ("PTR","HE1"):"HA", ("PTR","HD2"):"HA", ("PTR","HB3"):"HC",
  ("PTR","HB2"):"HC", ("PTR","HO3P"):"HP", ("PTR","HO2P"):"HP",("M3L","N"):"N",("M3L","NZ"):"N3",("M3L","CM3"):"HC", ("M3L","CA"):"HC",("M3L","CD"):"HC",
    ("M3L","CB"):"HC",("M3L","CG"):"HC",("M3L","CE"):"HC",("M3L","CM1"):"HC",
       ("M3L","CM2"):"HC",("M3L","C"):"C",("M3L","O"):"O",("M3L","OXT"):"OH",
 ("M3L","H"):"H", ("M3L","H2"):"H", ("M3L","HA"):"H1",("M3L","HM33"):"HC",
("M3L","HB2"):"HC",("M3L","HB3"):"HC",("M3L","HG2"):"HC",("M3L","HG3"):"HC",
("M3L","HD2"):"HC",("M3L","HD3"):"HC",("M3L","HM11"):"HC",("M3L","HM12"):"HC",
("M3L","HM13"):"HC",("M3L","HM21"):"HC",("M3L","HM22"):"HC",("M3L","HM23"):"HC",
("M3L","HM31"):"HC",("M3L","HM32"):"HC", ("M3L","HE2"):"HP", ("M3L","HE3"):"HP",("M3L","HXT"):"HO",("KCX","N"):"N",("KCX","NZ"):"N", ("KCX","CE"):"CT",  ("KCX","CA"):"CT",   ("KCX","CD"):"CT",
    ("KCX","CB"):"CT",     ("KCX","CG"):"CT", ("KCX","CX"):"C",  ("KCX","C"):"C", ("KCX","O"):"O",
 ("KCX","OQ1"):"O", ("KCX","OXT"):"OH", ("KCX","OQ2"):"OH", ("KCX","HZ"):"H",  ("KCX","HN2"):"H",
   ("KCX","H"):"H",("KCX","HA"):"H1", ("KCX","HD3"):"HC",  ("KCX","HD2"):"HC",   ("KCX","HG3"):"HC",
    ("KCX","HG2"):"HC",     ("KCX","HB3"):"HC",      ("KCX","HB2"):"HC", ("KCX","HE2"):"HP", ("KCX","HE3"):"HP",
 ("KCX","HQ2"):"HO", ("KCX","HXT"):"HO",("JLP","N"):"N",("JLP","NZ"):"N2",("JLP","N1"):"NC",("JLP","CA"):"CT",
 ("JLP","C"):"C",  ("JLP","C3"):"C",   ("JLP","C4"):"C", ("JLP","C2A"):"CT",
  ("JLP","CB"):"CT",   ("JLP","CD"):"CT",    ("JLP","CG"):"CT",     ("JLP","CE"):"CT",
      ("JLP","C4A"):"CT",       ("JLP","C5A"):"CT", ("JLP","C2"):"CA",
  ("JLP","C5"):"CA", ("JLP","C6"):"CA",("JLP","O"):"O",("JLP","O1"):"OH", ("JLP","O3"):"OH", ("JLP","OP4"):"OH",
 ("JLP","H1"):"H", ("JLP","H2"):"H", ("JLP","H4"):"H1",
 ("JLP","H13"):"H1", ("JLP","H10"):"HC",  ("JLP","H15"):"HC",
   ("JLP","H16"):"HC",    ("JLP","H19"):"HC",     ("JLP","H20"):"HC",      ("JLP","H21"):"HC",       ("JLP","H5"):"HC",        ("JLP","H6"):"HC",         ("JLP","H7"):"HC",          ("JLP","H9"):"HC",
           ("JLP","H8"):"HC", ("JLP","H11"):"HP", ("JLP","H12"):"HP", ("JLP","H17"):"HO",  ("JLP","H14"):"HO", ("JLP","H22"):"HO",
("JLP","H18"):"HA",("CME","N"):"N", ("CME","CZ"):"CT",  ("CME","CE"):"CT",   ("CME","CB"):"CT",    ("CME","CA"):"CT", ("CME","C"):"C", ("CME","O"):"O", ("CME","OXT"):"OH",
 ("CME","OH",):"OH", ("CME","SG"):"S", ("CME","SDS"):"S", ("CME","H"):"H", ("CME","H2"):"H",("CME","HA"):"H1",  ("CME","HE3"):"H1",   ("CME","HE2"):"H1",
    ("CME","HB3"):"H1", ("CME","HB2"):"H1",("CME","HZ3"):"HC",("CME","HZ2"):"HC",("HYP","N"):"N", ("HYP","HD23"):"H1",  ("HYP","HD22"):"H1",   ("HYP","HA"):"H1",
("HYP","C"):"C", ("HYP","CD"):"CT",  ("HYP","CG"):"CT",   ("HYP","CB"):"CT",    ("HYP","CA"):"CT",
 ("HYP","O"):"O", ("HYP","OD1"):"O2", ("HYP","OXT"):"OH", ("HYP","HB3"):"HC",  ("HYP","HB2"):"HC",   ("HYP","HG"):"HC",("HYP","H"):"G", ("HYP","HD1"):"HO",
 ("HYP","HXT"):"HO",
 ("CME","HH"):"HO", ("CME","HXT"):"HO",("CGU", "N"):"N,", ("CGU","CD2"):"C",  ("CGU","CD1"):"C",   ("CGU","C"):"C",
 ("CGU","CG"):"CT",  ("CGU","CA"):"CT",   ("CGU","CB"):"CT", ("CGU","O"):"O",
  ("CGU","OE11"):"O",   ("CGU","OE21"):"O",("CGU","OXT"):"OH", ("CGU","OE12"):"O2", ("CGU","OE22"):"O2", ("CGU","H"):"H",
 ("CGU","HN2"):"H", ("CGU","HA"):"H1", ("CGU","HE22"):"HO",  ("CGU","HE12"):"HO",   ("CGU","HXT"):"HO", ("CGU","HG"):"HC",
 ("CGU","HB2"):"HC",  ("CGU","HB3"):"HC",("HIC","N"):"N", ("HIC","NE2"):"NB",  ("HIC","ND1"):"NB",("HIC","C"):"C",
 ("HIC","CZ"):"CT",  ("HIC","CA"):"CT", ("HIC","CB"):"CT",("HIC","CG"):"CC",
("HIC","CD2"):"CV",("HIC","CE1"):"CR",("HIC","O"):"O",("HIC","OXT"):"OH",
("HIC","H"):"H",("HIC","H2"):"H",("HIC","HA"):"H1", ("HIC","HB2"):"HC",
 ("HIC","HB3"):"HC",("HIC","HD2"):"H4",("HIC","HE1"):"H5", ("HIC","HZ3"):"HC",
  ("HZ1","HZ3"):"HC",   ("HZ2","HZ3"):"HC", ("HZ2","HXT"):"HO",("GYS","N"):"N3",("GYS","N2"):"NB",("GYS","N3"):"N*", ("GYS","O2"):"O",
 ("GYS","O"):"O", ("GYS","OG1"):"OH", ("GYS","OH"):"OH",("GYS","OXT"):"OH",
 ("GYS","HD1"):"HA",  ("GYS","HE1"):"HA",   ("GYS","HE2"):"HA",    ("GYS","HD2"):"HA",
     ("GYS","HB2"):"HA", ("GYS","HXT"):"HO",  ("GYS","HOH"):"HO",   ("GYS","HG1"):"HO",
 ("GYS","C"):"C",  ("GYS","CA2"):"C",   ("GYS","C2"):"C",    ("GYS","CB2"):"C",
     ("GYS","CZ"):"C", ("GYS","CE2"):"CA",  ("GYS","CE1"):"CA",   ("GYS","CD2"):"CA",
    ("GYS","CD1"):"CA",     ("GYS","CG2"):"CA", ("GYS","CA1"):"CT",  ("GYS","CB1"):"CT",
   ("GYS","CA3"):"CT",("GYS","C1"):"CC", ("GYS","HN1"):"H", ("GYS","HN2"):"H",
 ("GYS","HA1"):"H1",  ("GYS","HA32"):"H1",   ("GYS","HA31"):"H1", ("GYS","HB12"):"HC",
 ("GYS","HB11"):"HC",("FME","N"):"N", ("FME","CN"):"C", ("FME","C"):"C", ("FME","CE"):"CT",
  ("FME","CG"):"CT",   ("FME","CB"):"CT",    ("FME","CA"):"CT", ("FME","SD"):"S",
 ("FME","H"):"H", ("FME","HCN"):"HO", ("FME","OXT"):"OH", ("FME","O1"):"O",
 ("FME","O"):"O", ("FME","HA"):"H1", ("FME","HB2"):"HC",  ("FME","HB3"):"HC",
 ("FME","HE3"):"H1",  ("FME","HE2"):"H1",   ("FME","HE1"):"H1",    ("FME","HG3"):"H1",
     ("FME","HG2"):"H1",("FME","HXT"):"HO",("DV9","N"):"N", ("DV9","CA"):"CT",  ("DV9","CB"):"CT",   ("DV9","CG"):"CT",
    ("DV9","C45"):"CT", ("DV9","CD"):"C", ("DV9","C"):"C", ("DV9","OE1"):"O",
  ("DV9","O15"):"O",   ("DV9","O"):"O",("DV9","OXT"):"OH", ("DV9","O14"):"OH",
 ("DV9","O16"):"OH",("DV9","FO1"):"F", ("DV9","FO2"):"F",("DV9","PO1"):"P",
 ("DV9","H4"):"HO",  ("DV9","H1"):"HO",   ("DV9","H59"):"HO", ("DV9","H2"):"H",
 ("DV9","H3"):"H",("DV9","H40"):"H1", ("DV9","H44"):"HC",  ("DV9","H42"):"HC",
   ("DV9","H41"):"HC",    ("DV9","H43"):"HC",("CYG","OXT"):"OH", ("CYG","HXT"):"HO",  ("CYG","HO2"):"HO", ("CYG","N"):"N",
 ("CYG","N1"):"N",("CYG","SG"):"S", ("CYG","OE2"):"O", ("CYG","O"):"O",
  ("CYG","O1"):"O", ("CYG","CG1"):"CT",  ("CYG","CA1"):"CT",   ("CYG","CA"):"CT",
    ("CYG","CB"):"CT",     ("CYG","CB1"):"CT", ("CYG","CD1"):"C", ("CYG","C1"):"C",
  ("CYG","C"):"C",("CYG","O2"):"OH", ("CYG","HN11"):"H",  ("CYG","HN12"):"H",
   ("CYG","H2"):"H",    ("CYG","H"):"H", ("CYG","HG12"):"H1",  ("CYG","HA"):"H1",
   ("CYG","HA1"):"H1",    ("CYG","HB2"):"H1",     ("CYG","HB3"):"H1",      ("CYG","HB13"):"H1",
       ("CYG","HB12"):"H1",        ("CYG","HG13"):"H1",("CR2","N2"):"N2",("CR2","N1"):"N3",("CR2","N3"):"N",("CR2","C3"):"C",
 ("CR2","CA1"):"CT", ("CR2","CA3"):"CT",("CR2","C1"):"CR", ("CR2","CZ"):"CA",
  ("CR2","CG2"):"CA",  ("CR2","CD1"):"CA",  ("CR2","CD2"):"CA",  ("CR2","CE1"):"CA",
  ("CR2","CE2"):"CA",  ("CR2","CA2"):"CC",   ("CR2","CB2"):"CC", ("CR2","C2"):"CC",
 ("CR2","O2"):"O", ("CR2","O3"):"O", ("CR2","OH"):"OH",  ("CR2","OXT"):"OH",
 ("CR2","HOH"):"HO", ("CR2","HXT"):"HO", ("CR2","HE2"):"HA",  ("CR2","HB2"):"HA",
   ("CR2","HD1"):"HA",    ("CR2","HD2"):"HA",     ("CR2","HE1"):"HA",      ("CR2","HN11"):"H", ("CR2","HN12"):"H",
 ("CR2","HA32"):"H1", ("CR2","HA12"):"H1",  ("CR2","HA31"):"H1",   ("CR2","HA11"):"H1",("CAS","N"):"N",("CAS","C"):"C",("CAS","O"):"O",("CAS","H2"):"H",
 ("CAS","H"):"H", ("CAS","CE2"):"CT",  ("CAS","CA"):"CT",   ("CAS","CB"):"CT",
    ("CAS","CE1"):"CT",("CAS","SG"):"SH", ("CAS","HE23"):"HC",  ("CAS","HE22"):"HC",
   ("CAS","HE21"):"HC",    ("CAS","HE13"):"HC",     ("CAS","HE12"):"HC",      ("CAS","HE11"):"HC",
 ("CAS","HB3"):"H1",  ("CAS","HB2"):"H1",   ("CAS","HA"):"H1",("CAS","HXT"):"HO",
("CAS","OXT"):"OH",("CAS","AS"):"OP",("BFD","N"):"N",("BFD","C"):"C", ("BFD","CG"):"C", ("BFD","O"):"O", ("BFD","OD2"):"O",
 ("BFD","CB"):"CT",  ("BFD","CA"):"CT", ("BFD","F3"):"F",  ("BFD","F2"):"F",
   ("BFD","F1"):"F", ("BFD","H2"):"H", ("BFD","H"):"H",("BFD","OXT"):"OH",
("BFD","HXT"):"HO",("BFD","OD1"):"OS",("BFD","HA"):"H1", ("BFD","HB2"):"HC",
 ("BFD","HB3"):"HC",("BFD","BE"):"C",("ALO","N"):"N",("ALO","C"):"C",("ALO","O"):"O", ("ALO","CG2"):"CT",  ("ALO","CA"):"CT",
   ("ALO","CB"):"CT",
 ("ALO","OG1"):"OH",
  ("ALO","OXT"):"OH",
 ("ALO","HG1"):"HO",
  ("ALO","HXT"):"HO",
 ("ALO","HG23"):"HC",
 ("ALO","HG22"):"HC",
 ("ALO","HG21"):"HC",("ALO","HB"):"H1",("ALO","HA"):"H1",("ALO","H2"):"H",("ALO","H"):"H",}

