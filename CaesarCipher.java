public class CaesarCipher {
    private char[] encoder = new char[26];
    private char[] decoder = new char[26];

    /**
     * Encrypt using ascii.
     * @param seed must be between 0 and 26, a number that adds pattern to encoder and decoder,
     */
    public CaesarCipher(int seed) {
        for (int index = 0; index < 26; index++) {
            encoder[index] = (char) ('A' + (index + seed) % 26); //gives a shifted alphabet
            decoder[index] = (char) ('A' + (index - seed + 26) % 26); //gives a shifted alphabet opposite way
        }

    }

    /**
     * Encrypts using transform method.
     * @param message message trying to encrypt, must be all caps.
     * @return encrypted message
     */
    public String encrypt(String message) {
        return transform(message, encoder);
    }

    /**
     * Decrypts using transform method.
     * @param message message trying to decrypt, will be all caps.
     * @return decrypted message
     */
    public String decrypt(String message) {
        return transform(message, decoder);
    }

    /**
     * Helper method for process of encoding and decoding
     * @param m message
     * @param coder encoder or decoder
     * @return encoded/decoded string
     */
    public String transform(String m, char[] coder) {
        char[] message = m.toCharArray();
        for (int x = 0; x < message.length; x++) {
            if (Character.isUpperCase(message[x])) {
                int num = message[x] - 'A';
                message[x] = coder[num];
            }
        }
        return new String(message);
    }

    /**
     * Code testing.
     * @param args args
     */
    public static void main(String[] args) {
        CaesarCipher cipher = new CaesarCipher(1);
        System.out.println("Encoder: " + new String(cipher.encoder));
        System.out.println("Decoder: " + new String(cipher.decoder));
        String message = "HELLO WORLD, I AM HERE TO TAKE OVER. DO NOT RESIST";
        String encrypted = cipher.encrypt(message);
        System.out.println(encrypted);
        String decrypted = cipher.decrypt(encrypted);
        System.out.println(decrypted);
    }

}
