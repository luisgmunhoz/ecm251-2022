
import java.util.ArrayList;
import java.util.List;

public class ValidadorCPF {
    private static List<Integer> cpfInvalido = new ArrayList<Integer>(){{add(1); add(1); add(3333333);}};

    public static boolean validar(String cpf) {
        cpf = cpf.replace(".", "");
        cpf = cpf.replace("-", "");
        // cpf = cpf.strip();
        if(cpf.length() != 11)
            return false;
        if (cpfInvalido.contains(cpf))
            return false;

        int soma = Integer.parseInt("" + cpf.charAt(0)) * 10;
        for(int i = 1; i < 9; i++)
            soma += Integer.parseInt("" + cpf.charAt(i)) * (10 - i);

        soma = (soma * 10) % 11;
        if (soma != Integer.parseInt("" + cpf.charAt(9)))
            return false;

        soma = Integer.parseInt("" + cpf.charAt(0)) * 11;
        for(int i = 1; i < 10; i++)
            soma += Integer.parseInt("" + cpf.charAt(i)) * (11 - i);
        soma = (soma * 10) % 11;
        if (soma != Integer.parseInt("" + cpf.charAt(10)))
            return false;

        return true;
    }
}