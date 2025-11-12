import gmpy2
import random
class RSA:
    @staticmethod
    def keyGeneration():
        """
        Generate RSA public and private keys using hardcoded primes.
        
        Returns:
            pk (list): Public key [e, n]
            sk (list): Private key [d, p, q]
        
        Note:
            p and q are hardcoded for educational purposes.
            In production, generate secure large primes dynamically.
        """
        p= 15554903035303856344007671063568213071669822184616101992595534860863803506262760067615727000088295330493705796902296102481798240988227195060316199080930616035532980617309644098719341753037782435645781436420697261984870969742096465765855782491538043554917285285471407866976465359446400695692459955929581561107496250057761324472438514351159746606737260676765872636140119669971105314539393270612398055538928361845237237855336149792618908050931870177925910819318623
        q= 15239930048457525970295803203207379514343031714151154517998415248470711811442956493342175286216470497855132510489015253513519073889825927436792580707512051299817290925038739023722366499292196400002204764665762114445764643179358348705750427753416977399694184804769596469561594013716952794631383872745339020403548881863215482480719445814165242627056637786302612482697923973303250588684822021988008175106735736411689800380179302347354882715496632291069525885653297
        phiN= (p-1)*(q-1)
        n = p*q
        while True:
            e = random.randrange(2, phiN)
            if gmpy2.gcd(e, phiN) == 1:
                break
        d = gmpy2.invert(e, phiN)
        pk = [e,n]
        sk = [d,p,q]
        return pk, sk
    
    @staticmethod
    def encryptFunction(message, pk):
        """
        Encrypt a plaintext message using the RSA public key.
        
        Args:
            message (str): The plaintext message to encrypt.
            pk (list): The public key [e, n].
        
        Returns:
            list: The encrypted message as a list of integers (ciphertext).
        """
        e, n = pk
        cipher = [pow(ord(char), e, n) for char in message]
        return cipher
    
    @staticmethod
    def decryptFunctionCRT(cipher, sk):
        """
        Decrypt an RSA ciphertext using the private key and the chinese remainder theorem optimization method.
        
        Args:
            cipher (list): The encrypted message as a list of integers.
            sk (list): The private key [d, p, q].
        
        Returns:
            str: The decrypted plaintext message.
        """
        d,p,q = sk
        dp = d % (p - 1)
        dq = d % (q - 1)
        qinv = gmpy2.invert(q, p)
        mp = [pow(char, dp, p) for char in cipher]
        mq = [pow(char, dq, q) for char in cipher]
        h = [(qinv * (mp[i] - mq[i])) % p for i in range(len(cipher))]
        message = ''.join([chr((mq[i] + h[i] * q) % (p * q)) for i in range(len(cipher))])
        return message 
    @staticmethod
    def RSAFunction(message):
        """
        Generate keys, encrypt the message, then decrypt it.
        
        Args:
            message (str): The plaintext message.
        
        Returns:
            tuple: (ciphertext list, decrypted plaintext string)
        """
        pk, sk = RSA.keyGeneration()
        cipherText = RSA.encryptFunction(message, pk)
        plainText = RSA.decryptFunctionCRT(cipherText, sk)
        return cipherText, plainText
def main():
    message = "Hello World!"
    cipherText, plainText = RSA.RSAFunction(message)
    print("Original Message:", message)
    print("Encrypted Message:", cipherText)
    print("Decrypted Message:", plainText)    

if __name__ == "__main__":
    main()