// Definition for singly-linked list.
// #[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
   pub val: i32,
   pub next: Option<Box<ListNode>>
}
 
impl ListNode {
    #[inline]
    fn new(val: i32) -> Self {
        ListNode {
            next: None,
            val: val,
        }
    }
    fn append(&mut self, val: i32) {
        match &mut self.next {
            Some(ref mut x) => x.append(val),
            None => {
                let n = ListNode {
                    val: val,
                    next: None,
                };
                self.next = Some(Box::new(n));
            },
        }
    }
    fn list(& self) {
        println!("{}", self.val);
        match &self.next {
            Some(x) => x.list(),
            None => {},
        }
    }
}

// 206. Reverse linked list
fn reverse_list (head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
    match head {
        Some(x) => {
            //println!("{}", x.val);
            match reverse_list(x.next) {
                Some(mut t) => {
                    t.append(x.val);
                    return Some(t);
                },
                None => {
                    return Some(Box::new(ListNode::new(x.val)));
                }
            }
        },
        None => {
            return None;
        },
    }
}

// 96. Reverse Linked List II
fn reverse_between(head: Option<Box<ListNode>>, left: i32, right: i32) -> Option<Box<ListNode>> {

}

fn main() {
    println!("Hello, world!");
    let reversedlistnode: Option<Box<ListNode>>;
    let mut listnode = ListNode::new(1);
    listnode.append(2);
    listnode.append(3);
    listnode.append(4);
    listnode.append(5);
    listnode.list();

    println!("========");

    reversedlistnode = reverse_list(Some(Box::new(listnode)));
    match reversedlistnode {
        Some(x) => {x.list();},
        None => {println!("NONE");}
    }
}
