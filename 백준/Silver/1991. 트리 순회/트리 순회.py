n=int(input())
left=[[] for i in range(n)]
right=[[] for i in range(n)]
for i in range(n):
    node,l,r=map(str,input().split())
    node=ord(node)-65
    if l!='.':
        left[node]=ord(l)-65
    if r!='.':
        right[node]=ord(r)-65

def preorder(idx):
    print(chr(idx+65),end='')
    if left[idx]!=[]:
        preorder(left[idx])
    if right[idx]!=[]:
        preorder(right[idx])

def inorder(idx):
    if left[idx]!=[]:
        inorder(left[idx])
    print(chr(idx+65),end='')
    if right[idx]!=[]:
        inorder(right[idx])

def postorder(idx):
    if left[idx]!=[]:
        postorder(left[idx])
    if right[idx]!=[]:
        postorder(right[idx])       
    print(chr(idx+65),end='')

preorder(0)
print("")
inorder(0)
print("")
postorder(0)
