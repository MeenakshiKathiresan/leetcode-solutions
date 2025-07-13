public class Solution {
    public int MatchPlayersAndTrainers(int[] players, int[] trainers) {
        // player abilities
        // trainer capacity
        // if trainer cap >= player ability ---> +1 
        Array.Sort(players);
        Array.Sort(trainers);

        // pointers for player and trainer
        int p = 0, t = 0, res = 0;

        while (p < players.Length && t < trainers.Length){
            if(players[p] <= trainers[t]){
                p++; 
                t++;
                res++;
            }else{
                t++;
            }

        }
        return res;
    }
}