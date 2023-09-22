public class RandomizedSet {
    Dictionary<int, int> randomNumbers = new Dictionary<int, int>();
    List<int> numberList = new List<int>();
    Random rnd = new Random();

    public RandomizedSet() {
        
    }
    
    public bool Insert(int val) {
        if (randomNumbers.ContainsKey(val)) {
            return false;
        }
        
        randomNumbers.Add(val, numberList.Count);
        numberList.Add(val);
        return true;
    }
    
    public bool Remove(int val) {
        if (!randomNumbers.ContainsKey(val)) {
            return false;
        }
        
     
        
        int ind = randomNumbers[val];
        int last = numberList[numberList.Count - 1];
        
        randomNumbers[last] = ind;
        numberList[ind] = last;
        
        numberList.RemoveAt(numberList.Count - 1);
        randomNumbers.Remove(val);
        
        return true;
    }
    
    public int GetRandom() {
        int randIndex = rnd.Next(numberList.Count);
        return numberList[randIndex];
    }
}
