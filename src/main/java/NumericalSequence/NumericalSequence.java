package NumericalSequence;
import java.util.List;
import java.util.ArrayList;

public class NumericalSequence {
    private static final String equation = "a^(n+1)*(a/(b*n-a))";

    private int a;
    private int b;
    private int max_number;
    private List<Float> sequence;

    public NumericalSequence(int a, int b, int max_numbers) {
        this.a = a;
        this.b = b;
        this.max_number = max_numbers;
        refreshSequence();
    }
    
    public double getA() {
        return a;
    }

    public double getB() {
        return b;
    }

    public int getMaxNumber() {
        return max_number;
    }

    public void setA(int a) {
        this.a = a;
        refreshSequence();
    }

    public void setB(int b) {
        this.b = b;
        refreshSequence();
    }

    public void setMaxNumber(int max_number) {
        this.max_number = max_number;
        refreshSequence();
    }

    public int calculateSum(int n, int start) throws Exception {
        if (n > max_number) {
            throw new Exception("Test");
        }
        int sum = 0;
        for (int i = start; i <= n; i++) {
            sum += calculateElement(i);
        }
        return sum;
    }

    public float calculateElement(int n) {
        return (float) (Math.pow(a, n + 1) * (a / (b * (float) n - a)));
    }

    public List<Float> calculateSequence(int k, int m) throws Exception {
        if (m > max_number) {
            throw new Exception("Input value is out of elements range");
        }
        List<Float> seq = new ArrayList<>();
        for (int i = k; i <= m; i++) {
            seq.add(calculateElement(i));
        }
        return seq;
    }

    public static void printSequence(NumericalSequence sequence) {
        System.out.print("a=" + sequence.a + ", b=" + sequence.b + ": ");
        for (Float element : sequence.sequence) {
            System.out.print(element + " ");
        }
        System.out.println();
    }

    public static void compareSequence(NumericalSequence sequence1, NumericalSequence sequence2) {
        if (sequence1.sequence.equals(sequence2.sequence)) {
            System.out.println("True. Sequences are equal");
        } else {
            System.out.println("False. Sequences are not equal");
        }
    }

    private void refreshSequence() {
        int lastElement = 7;
        if (max_number < 7) {
            lastElement = max_number;
        }
        List<Float> sequence = null;
        try {
            sequence = calculateSequence(1, lastElement);
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
        this.sequence=sequence;
        printSequence(this);
    }
}
