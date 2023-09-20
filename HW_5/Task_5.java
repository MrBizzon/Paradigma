public class Task_5 {
    public static int arraySum(int[] arr) {
        int sum = 0;
        for (int i = 0; i < arr.length; i++) {
            sum += arr[i];
        }
        return sum;
    }

    public static void main(String[] args) {
        int[] array = {1, 2, 3, 4, 5};
        int sum = arraySum(array);
        System.out.println("Sum of array elements: " + sum);
    }
}