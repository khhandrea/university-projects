import Math;

public class Assignment_14_2 {
    public static String delChar(String src, String delCh) {
        StringBuffer result = new StringBuffer(src);
        int index;
        
        for(int i = 0; i < delCh.length(); i++) {
            index = result.indexOf("" + delCh.charAt(i));
            while(index != -1) {
                result.delete(index, index + 1);
                index = result.indexOf("" + delCh.charAt(i));
            }
        }

        return result.toString();
    }

    public static void main(String[] args) {
        System.out.println("(1!2@3^4~5)" + " → " + delChar("(1!2@3^4~5)", "~!@#$%^&*()"));
        System.out.println("(1 2    3   4\t5)" + " → " + delChar("(1 2  3   4\t5)", " \t"));
    }
}