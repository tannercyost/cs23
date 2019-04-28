import java.util.*;

/**
 *
 * @author tanner yost
 */
public class TruthTables {
    /**
     * method getLength returns the number of propositions in the statement
     * @param tokens
     * @return
     */
    private static int GetLength(Set<String> tokens) {
        int length = 0;
        for (String token : tokens) {
            if (null == token) {
                System.out.println("Empty string detected.");
            }
            else switch (token) {
                case "=":
                    break;
                case "->":
                    break;
                case "<=":
                    break;
                case "+":
                    break;
                case "*":
                    break;
                case "!":
                    break;
                case "~":
                    break;
                case "True":
                    break;
                case "False":
                    break;
                default:
                    length++;
                    break;
            }
        }

        return length;
    }

    /**
     * method getInput returns the provided input for later use
     * @return
     */
    private static String[] GetInput() {

        char[] tokens;
        Scanner sc = new Scanner(System.in);
        Set<String> inputSet = new HashSet<>();

        String input = sc.nextLine();
        //String input = "p p * r *";
        String expression[] = input.split(" ");
        String[] trimmedArray = new String[expression.length];
        for (int i = 0; i < expression.length; i++) {
            trimmedArray[i] = expression[i].trim();
        }

        return trimmedArray;

    }
    private static Set createSet(String[] a) {
        Set<String> inputSet = new HashSet<>();

        for(String token : a){
            inputSet.add(token);
        }
        return inputSet;
    }

    /**
     * method print truth table will provide a truth table, based on the number of propositions.
     * It will then populate the table, for each propositions it will provide a true/false value.
     * Then it will send these values into calculateTruth which will print out on the last column the truth value of the entire statement
     * @param n, length
     * @param st
     * @param propositions
     */
    private static void PrintTruthTable(int n, Set<String> input, String[] inputString) {
        int rows = (int) Math.pow(2,n);
        HashMap propositions;
        for (int i=0; i<rows; i++) { // for each row
            boolean[] truth = new boolean[n];
            for (int j=n-1; j>=0; j--) {
                int value = ((i/(int) Math.pow(2, j))%2);
                if(value == 1){
                    truth[j] = true;
                    System.out.print(truth[j]);
                    System.out.print("\t");
                }
                else if (value == 0){
                    truth[j] = false;
                    System.out.print(truth[j]);
                    System.out.print("\t");
                }
            }

            propositions = LinkMap(truth, n, input);
            System.out.println(CalculateTruth(n, propositions, inputString));
            //System.out.println(propositions);
        }
    }
    /**
     * method calculateTruth returns the truth value
     * @param st
     * @param propositions
     */
    private static Boolean CalculateTruth(int length, HashMap propositions, String[] input){
        ArrayList<Boolean> operands = new ArrayList<>();
        int numberOfPushes = 0;
        Stack<Boolean> st = new Stack<>();

        for (String token : input) {
            if (null == token) {
                System.out.println("Empty string detected.");
            }
            else switch (token) {
                case "=":
                    operands.clear();
                    operands.add(st.pop());
                    operands.add(st.pop());
                    st.push(operands.get(0) == operands.get(1));
                    break;
                case "->":
                    operands.clear();
                    operands.add(st.pop());
                    operands.add(st.pop());
                    st.push(operands.get(0) || !operands.get(1));
                    break;
                case "<=":
                    operands.clear();
                    operands.add(st.pop());
                    operands.add(st.pop());
                    st.push(operands.get(0) || !operands.get(1));
                    break;
                case "+":
                    operands.clear();
                    operands.add(st.pop());
                    operands.add(st.pop());
                    st.push(operands.get(0) || operands.get(1));
                    break;
                case "*":
                    operands.clear();
                    operands.add(st.pop());
                    operands.add(st.pop());
                    st.push(operands.get(0) && operands.get(1));
                    break;
                case "!":
                    operands.clear();
                    operands.add(st.pop());
                    st.push(!operands.get(0));
                    break;
                case "~":
                    operands.clear();
                    operands.add(st.pop());
                    st.push(!operands.get(0));
                    break;
                case "True":
                    operands.clear();
                    operands.add(true);
                    st.push(true);
                    break;
                case "False":
                    operands.clear();
                    operands.add(false);
                    st.push(false);
                    break;
                default:
                    st.push((Boolean) propositions.get(token));
                    numberOfPushes++;
                    break;
            }
        }
        Boolean truthValue = st.pop();
        return truthValue;
    }
    /**
     * method linkMap will create a hashmap for the truth values of the propositions
     */
    private static HashMap LinkMap(boolean[] truth, int n, Set<String> input) {
        HashMap<String, Boolean> propositions = new HashMap<>();

        int j = n-1;
        System.out.println(j);
        for (String token : input) {
                if (null == token) {
                    System.out.println("Empty string detected.");
                }
                else switch (token) {
                    case "=":
                        break;
                    case "->":
                        break;
                    case "<=":
                        break;
                    case "+":
                        break;
                    case "*":
                        break;
                    case "!":
                        break;
                    case "~":
                        break;
                    case "True":
                        break;
                    case "False":
                        break;
                    default:
                        propositions.put(token, truth[j]);
                        j--;
                        break;
                }
        }

        return propositions;
    }
    /**
     * Prints the first row of the truth table, the header.
     * Contains all of the propositions to be examined as well as a column for the whole statement.
     * @param length, integer representing how many propositions there are
     * @param input, the string representing the entire input. Separated by whitespace and then printed.
     */
    private static void PrintHeader(int length, Set<String> input, String[] inputString) {
        List<String> sortedList = new ArrayList<>();


        if(length>0) {
            for (String token : input) {
                if (null == token) {
                    System.out.println("Empty string detected.");
                }
                else switch (token) {
                    case "=":
                        break;
                    case "->":
                        break;
                    case "<=":
                        break;
                    case "+":
                        break;
                    case "*":
                        break;
                    case "!":
                        break;
                    case "~":
                        break;
                    case "True":
                        break;
                    case "False":
                        break;
                    default:
                        sortedList.add(token);
                        break;
                }
            }

            Collections.sort(sortedList);
            for(String a : sortedList){
                System.out.print(a);
                System.out.print("\t");
            }

            for(String element : inputString){
                System.out.print(element);
                System.out.print(" ");
            }
            System.out.println("");
        }

    }
    public static void main(String[] args) {
        Set<String> inputSet = new HashSet<>();
        String[] input = GetInput();
        inputSet = createSet(input);
        int length = GetLength(inputSet);
        System.out.println(length);
        PrintHeader(length, inputSet, input);
        PrintTruthTable(length, inputSet, input);
    }
}
