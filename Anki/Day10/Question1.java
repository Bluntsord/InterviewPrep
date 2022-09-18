package Anki.Day10;

import java.util.*;

public class Question1 {
  public static HashMap<String, List<String>> accountNeighbours;
  public static HashMap<String, Boolean> visited;

  public static void main(String[] args) {
    List<List<String>> accounts = List.of(
        List.of("John","johnsmith@mail.com","john_newyork@mail.com"),
        List.of("John","johnsmith@mail.com","john00@mail.com"),
        List.of("Mary","mary@mail.com"),
        List.of("John","johnnybravo@mail.com")
    );

    List<List<String>> answer = accountsMerge(accounts);
    System.out.println(answer);
  }

  public static List<List<String>> accountsMerge(List<List<String>> accounts) {
    accountNeighbours = generateAccountNeighbours(accounts);
    visited = new HashMap<>();
    List<List<String>> answer = new ArrayList<>();
    for (List<String> account: accounts) {
      answer.add(Dfs(account, visited));
    }
    return answer;
  }

  public static List<String> Dfs(List<String> account, HashMap<String, Boolean> visited) {
    String name = account.get(0), start = account.get(1);
    Stack<String> stack = new Stack<>();
    stack.add(start);
    visited.put(start, Boolean.TRUE);
    List<String> answer = new ArrayList<>();

    while (!stack.empty()) {
      String curr_node = stack.pop();
      answer.add(curr_node);
      List<String> neighbours = accountNeighbours.getOrDefault(curr_node, new ArrayList<>());

      for (String neighbour: neighbours) {
        if (!visited.containsKey(neighbour)) {
          visited.put(neighbour, Boolean.TRUE);
          stack.add(neighbour);
        }
      }
    }

    return answer;
  }

  public static HashMap<String, List<String>> generateAccountNeighbours(List<List<String>> accounts) {
    HashMap<String, List<String>> accountsNeighbours = new HashMap<>();
    for (List<String> account: accounts) {
      if (account.size() == 2) {
        continue;
      }

      for (int i = 1; i < account.size() - 1; i++) {
        String firstAccount = account.get(i);
        String secondAccount = account.get(i + 1);
        List<String> firstAccountConnections = accountsNeighbours.getOrDefault(firstAccount, new ArrayList<>());
        firstAccountConnections.add(secondAccount);
        accountsNeighbours.put(firstAccount, firstAccountConnections);

        List<String> secondAccountConnections = accountsNeighbours.getOrDefault(secondAccount, new ArrayList<>());
        secondAccountConnections.add(firstAccount);
        accountsNeighbours.put(secondAccount, secondAccountConnections);
      }
    }

    return accountsNeighbours;
  }
}

