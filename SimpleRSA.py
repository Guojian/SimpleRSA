import random,fractions
class RSA:
    def is_prime(self,a, s, d, n):
        v = pow(a, d, n)
        if v == 1:
            return True
        for i in xrange(s-1):
            if v == n - 1:
                return True
            v = pow(v,2,n)
        return v == n - 1


    def determine_prime(self,n):
        d = n - 1
        s = 0
        while d % 2 == 0:#calculate 2^s*d
            d >>= 1
            s += 1
            
        for repeat in xrange(20):
            a = 0
            while a == 0:
                a = random.randrange(n)
            if not self.is_prime(a, s, d, n):
                return False
        return True

    def genprimenum(self,numbits):
            while True:
                    p = random.getrandbits(int(self.bits))
                    if p < 0:continue
                    if self.determine_prime(p):
                            #print p
                            return p
                            
    def returngcd(self,a,b):
            if b==0:
                    x0=1
                    y0=0
                    return [a,x0,y0]
            temp = self.returngcd(b,a%b)
            d = temp[0]
            t = temp[1]
            x = temp[2]
            y = t - a/b*temp[2]
            return [d,x,y]

    def genKeys(self,bits):
        
            self.bits = bits
            p = self.genprimenum(self.bits)
            q = self.genprimenum(self.bits)
            n = p*q
            nn = (p-1) * (q-1)
            while True:
                    e1 = random.getrandbits(int(self.bits))
                    if fractions.gcd(e1,nn)==1:
                            e2 = self.returngcd(e1,nn)[1]
                            if e2 > 0:
                                    
                                    #print 'e1 = ', e1
                                    #print 'e2 = ', e2
                                    break
           
            assert e1<n
            assert e2<n
            assert fractions.gcd(e1,nn)==1
            assert e1*e2%nn ==1
            keys = [(n,e1),(n,e2)]
            return keys
        
    def encrypt(self,key,msg):
        splitmsgnum = len(msg)/10 + 1
        textmsg = []
        ciphermsg = []
        for i in range(0,splitmsgnum):
                submsg = msg[i*10:10*(i+1)]#10 characters is a block
                if len(submsg)<10:
                        submsg = submsg + ' '*(10-len(submsg))
                textmsg.append(submsg)
                subcipher = ''
                for i in range(0,len(submsg)):
                        temp = '%03.0f' %ord(submsg[i])
                        subcipher += str(temp)
                ciphermsg.append(subcipher)
        encriptmsg = []        
        e = key[1]
        n = key[0]
        encryptmsg = []
        for i in range(0,len(ciphermsg)):
                encript = pow(long(ciphermsg[i]),e,n)
                encryptmsg.append(str(encript))
        return encryptmsg
        
    def decrypt(self,key,encryptmsg):
        cleartext = ''
        for subencryptmsg in encryptmsg:                 
        #decription 
            e = key[1]
            n = key[0]
            decripting = pow(long(subencryptmsg),e,n)            
        #Print msg
            decripting = str(decripting)
            if len(decripting)%3 == 2:
                    decripting = '0' + decripting
            if len(decripting)%3 == 1:     
                    decripting = '00' + decripting                         
            subcleartext = ''
            for i in range(len(decripting)/3-1,-1,-1):
                    subcleartext = chr(long(decripting[i*3:(i+1)*3])) + subcleartext
            cleartext = cleartext + subcleartext        
        return cleartext

if __name__=='__main__':
    rsa = RSA()
    bits = raw_input('Please input your bits:')
    keys = rsa.genKeys(bits)
    msg = raw_input('Please input the msg:')
    key1 = keys[0]
    key2 = keys[1]
    enmsg = rsa.encrypt(key1,msg)
    print 'Follwing is encrypt msg'
    print enmsg
    print 'Follwing is decrypt msg'
    demsg = rsa.decrypt(key2,enmsg)
    print demsg

