   var stack = new buckets.Stack();
        var pushMe = function(){
            pushItem = document.createElement("li");
            pushItem.innerText = document.getElementById("names").value;
            stack.add(pushItem)
            document.getElementById("listitems-stack").appendChild(pushItem);
        }
        var popMe = function(){   
            if(stack.size()!=0)
            {
                var popItem = stack.pop();
                document.getElementById("listitems-stack").removeChild(popItem);
            }
        }
        var queue = new buckets.Queue();
        var queueMe = function(){
            queueItem = document.createElement("li");
            queueItem.innerText = document.getElementById("names").value;
            //Add to queue and to the UI
            queue.enqueue(queueItem)
            document.getElementById("listitems-queue").appendChild(queueItem);

        }
        var dequeueMe = function(){
            if(queue.size()!=0)
            {
                //Remove from the queue and the UI
                var dequeueItem = queue.dequeue();
                document.getElementById("listitems-queue").removeChild(dequeueItem);
            }
        }
        
              