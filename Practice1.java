
import java.util.Scanner;
  
public class Practice1 {
	//답을 만들어 놓는 곳
	public int solution(String str, char t){
		int answer = 0;
		
		//모두 대문자로 바꾸기
		str=str.toUpperCase();
		t=Character.toUpperCase(t);
		
		/*for (int i=0; i<str.length(); i++) {
			if(str.charAt(i)==t) answer++;
		}*/
		
		for(char X : str.toCharArray()) {
			if (X == t) answer++;
		}
				
		return answer;
	}
	
	
  public static void main(String[] args){
    
	 Practice1 T = new Practice1();
	 
	 //입력받기
	 Scanner kb = new Scanner(System.in);
	 String str = kb.next(); //문자열을 콘솔로 읽어들임
	 char c = kb.next().charAt(0);  //문자열에서 문자 하나 읽어들이기
	 
	 //솔루션 호출 >> 리턴 받은 것을 출력한다.
	 System.out.print(T.solution(str, c));
	 
    
    return ;
  }
}

