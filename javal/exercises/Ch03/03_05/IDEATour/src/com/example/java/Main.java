package com.example.java;

import java.util.*;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        System.out.println("Hello from IDEA!");
        String aString = "David";
        System.out.println("Your name is " + aString);
        float f = 7.0f;
        System.out.println(f);
        String s = "Rajesh Padmanabhan";
        char[] c = s.toCharArray();
        for (char c1 : c) {
            System.out.println(c1);
        }

        Scanner sc= new Scanner(System.in);
        String k = sc.nextLine();
        System.out.println(k+":"+k.length());
        Map<String,String> m = new HashMap<>();
        m.put("First","Rajesh");
        m.put("Last","Padmanabhan");
        System.out.println((m));
    }

}

