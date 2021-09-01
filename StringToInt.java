
public class StringToInt {
	
	public static int ConvertInt(String str) {
		int result = 0;
		for(int i = 0; i < str.length(); i++) {
			char a = str.charAt(i);
			int num = a - 48;
			num *= Math.pow(10, (str.length() - i - 1));
			result += num;
		}
		
		return result;
	}
	
	
	// integer without using functions
	public static int convert(String s) {
		// Initialze a variable
		int num = 0;
		int n = s.length();
		
		// Iterate till ength of the string
		for(int i = 0; i < n; i++) {
			num = num * 10 + ((int)s.charAt(i) - 48);
			System.out.println(num);
		}
		return num;
	}
	
	
	public static void main(String[] args) {
		System.out.println(ConvertInt("123"));
		System.out.println(convert("456"));
	}

}
