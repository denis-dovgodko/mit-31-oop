package com.lab1.lab1task2;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import NumericalSequence.NumericalSequence;


@SpringBootApplication
public class Lab1Task2Application {

    public static void main(String[] args) throws Exception {
        SpringApplication.run(Lab1Task2Application.class, args);
        NumericalSequence sequence1 = new NumericalSequence(1, 2, 20);

        System.out.println(sequence1.calculateElement(1));
        System.out.println(sequence1.calculateElement(2));

        System.out.println(sequence1.calculateSum(2, 1));
        System.out.println(sequence1.calculateSum(3, 2));

        System.out.println(sequence1.calculateSequence(2, 4));

        NumericalSequence sequence2 = new NumericalSequence(3, 4, 8);

        NumericalSequence.compareSequence(sequence1, sequence2);

        sequence2.setA(1);
        sequence2.setB(2);

        NumericalSequence.compareSequence(sequence1, sequence2);

        sequence2.setMaxNumber(6);

        NumericalSequence.compareSequence(sequence1, sequence2);
    }
}
