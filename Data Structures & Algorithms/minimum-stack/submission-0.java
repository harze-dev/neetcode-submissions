class MinStack {

    private List<Integer> list;
    private List<Integer> minList;

    public MinStack() {
        list = new ArrayList<>();
        minList = new ArrayList<>();
    }
    
    public void push(int val) {
        // 1 2 0
        // 1 1 0

        list.add(val);
        if(!list.isEmpty() & getMin() > val ){
            minList.add(val);
        }
        else if(!minList.isEmpty()){
            int prev = minList.get(minList.size() - 1);
            minList.add(prev);
        }
        else{
            minList.add(val);
        }
        
    }
    
    public void pop() {
        if (!list.isEmpty()) { 
            list.remove(list.size() - 1);
            minList.remove(minList.size()- 1);
        }
    }
    
    public int top() {
        if (!list.isEmpty()) { 
            return list.get(list.size() - 1); 
        }

        return -1;
    }
    
    public int getMin() {
        if (!minList.isEmpty()) { 
            return minList.get(minList.size() - 1); 
        }

        return -1;
    }
}
