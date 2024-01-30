import java.util.*;

public class Stable_Matching_Problem_Example {
    public static void main(String[] args) {
        // Example preferences for men and women
        Map<String, List<String>> menPreferences = new HashMap<>();
        menPreferences.put("Man1", Arrays.asList("Woman1", "Woman2", "Woman3"));
        menPreferences.put("Man2", Arrays.asList("Woman2", "Woman1", "Woman3"));
        menPreferences.put("Man3", Arrays.asList("Woman3", "Woman1", "Woman2"));

        Map<String, List<String>> womenPreferences = new HashMap<>();
        womenPreferences.put("Woman1", Arrays.asList("Man3", "Man1", "Man2"));
        womenPreferences.put("Woman2", Arrays.asList("Man1", "Man2", "Man3"));
        womenPreferences.put("Woman3", Arrays.asList("Man2", "Man1", "Man3"));

        // Run the stable matching algorithm
        Map<String, String> matching = stableMatching(menPreferences, womenPreferences);

        // Print the stable matching
        System.out.println("Stable Matching:");
        for (Map.Entry<String, String> entry : matching.entrySet()) {
            System.out.println(entry.getKey() + " matches " + entry.getValue());
        }
    }

    // Gale-Shapley stable matching algorithm
    private static Map<String, String> stableMatching(Map<String, List<String>> menPreferences,
                                                      Map<String, List<String>> womenPreferences) {
        Map<String, String> matching = new HashMap<>();
        List<String> freeMen = new ArrayList<>(menPreferences.keySet());

        // While there are free men
        while (!freeMen.isEmpty()) {
            String man = freeMen.remove(0);
            List<String> preferences = menPreferences.get(man);

            // Iterate through the man's preferences
            for (String woman : preferences) {
                // If the woman is not yet matched, pair them
                if (!matching.containsValue(woman)) {
                    matching.put(man, woman);
                    break;
                } else {
                    // If the woman is already matched, check if she prefers the current man
                    String currentMan = getKeyByValue(matching, woman);
                    List<String> womanPreferences = womenPreferences.get(woman);

                    // If the woman prefers the current man over the new man, break the existing pair
                    if (womanPreferences.indexOf(man) < womanPreferences.indexOf(currentMan)) {
                        matching.put(man, woman);
                        freeMen.add(currentMan);
                        break;
                    }
                }
            }
        }

        return matching;
    }

    // Helper method to get the key by value in a map
    private static <K, V> K getKeyByValue(Map<K, V> map, V value) {
        for (Map.Entry<K, V> entry : map.entrySet()) {
            if (Objects.equals(value, entry.getValue())) {
                return entry.getKey();
            }
        }
        return null;
    }
}
