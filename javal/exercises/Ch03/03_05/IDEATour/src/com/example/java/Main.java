package com.example.java;

import com.sun.tools.doclets.formats.html.SourceToHTMLConverter;

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
        Map<String,String> m = new HashMap<>();
        Scanner sc= new Scanner(System.in);
        String k = "start";
        while (!k.equals("exit"))
        {
            k = sc.nextLine();
            System.out.println(k);
            if (!k.equals("exit"))
            {
                m.put(k,Integer.toString(k.length()));

            }
            else
            {
                break;
            }
        }
        System.out.println((m));
    }

}

