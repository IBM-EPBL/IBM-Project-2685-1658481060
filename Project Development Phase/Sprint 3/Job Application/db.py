import ibm_db
try:

 conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=ea286ace-86c7-4d5b-8580-3fbfa46b1c66.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;PORT=31505;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=zxy98776;PWD=oy5RDl5H6O1w1Jpd",'','')
 print("db is connected")
except:
    print("db is not connected")