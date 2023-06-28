import Model.Toy;

import java.io.FileWriter;
import java.io.IOException;
import java.util.PriorityQueue;
import java.util.Random;

public class Main {
    private static final String FILENAME = "results.txt";
    private static final int NUM_CALLS = 10; // Количество вызовов getToy()
    public static void main(String[] args) {
        // Создание и заполнение коллекции игрушек
        PriorityQueue<Toy> toys = new PriorityQueue<>();
        toys.offer(new Toy(1, "робот", 2));
        toys.offer(new Toy(2, "кукла", 6));
        toys.offer(new Toy(3, "машина", 4));
        toys.offer(new Toy(4, "констрктор", 3));
        toys.offer(new Toy(5, "пазлы", 1));
        toys.offer(new Toy(6, "мячик", 2));
        // Выполнение вызовов getToy() и запись результатов в файл
        try {
            FileWriter writer = new FileWriter(FILENAME);
            Random random = new Random();
            for (int i = 0; i < NUM_CALLS; i++) {
                int randomNumber = random.nextInt(10) + 1; // Случайное число от 1 до 10
                Toy toy = getToy(toys, randomNumber);
                writer.write(toy.toString() + "\n");
            }
            writer.close();
            System.out.println("Результаты записаны в файл " + FILENAME);
        } catch (IOException e) {
            e.printStackTrace();
        }

    }
    private static Toy getToy(PriorityQueue<Toy> toys, int randomNumber) {
        int cumulativeWeight = 0;
        int totalWeight = toys.stream().mapToInt(Toy::getWeight).sum();

        for (Toy toy : toys) {
            cumulativeWeight += toy.getWeight();
            double probability = (double) cumulativeWeight / totalWeight;
            if (randomNumber <= probability * 10) {
                return toy;
            }
        }

        // Если не удалось определить игрушку на основе случайного числа, вернуть последний элемент очереди
        return toys.peek();
    }

}
