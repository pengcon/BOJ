

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Scanner;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//		Scanner sc = new Scanner(System.in);
		int n = Integer.parseInt(br.readLine());
		int m = Integer.parseInt(br.readLine());
		int [] A = new int[n];
		StringTokenizer st = new StringTokenizer(br.readLine());
		for (int i = 0; i<n ; i++) {
			A[i]=Integer.parseInt(st.nextToken());
		}
		Arrays.sort(A);
		int count=0;
		int start=0;
		int end=n-1;
		while (start<end) {
			
			if (A[start]+A[end]>m) {
				end-=1;
			}
			else if (A[start]+A[end]<m){
				start+=1;
			}
			else if (A[start]+A[end]==m) {
				count+=1;
				start+=1;
				end-=1;
			}
		}
		System.out.println(count);
			
		
		
	}

}
