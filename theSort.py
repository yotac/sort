class objectInTheList():
    def _init_(self,data,dataN):
        self.data=data
        self.dataN=dataN

    def _add_(self,o):
        self.data=self.data+o.data
        return self

    def _lt_(self, other):
        if(self.data<other.data):
            return True
        else:
            return False

    def _le_(self, other):
        if self.dataN<other.dataN:
            return True
        elif self.dataN==other.dataN:
            return True
        else:
            return False

    def _str_(self):
        return self.data+" : "+str(self.dataN)

def SPLIT(string):
    listr=[]
    for i in range(string.count(" ")+1):
        w=string.find(" ")
        data=string[:w]
        listr.append(objectInTheList(string[:w],dataN=1))
        string=string[w+1:]
    w=len(listr)-1
    tmp=objectInTheList(string[len(string)-1],1)
    listr[w]=listr[w]+tmp
    return listr

def find(lst,o):
  for i in range(len(lst)):
    if lst[i].data==o:
      return True

def popMe(lst,o):
  for i in range(len(lst)):
    if lst[i].data==o:
      lst.pop(i)
      return lst

def PrepareTheString(f):
    punctuation='!"#$%&()*+,-./:;<=>?@[]^_`{|}~'
    string=f.read()
    string=string.lower()
    for i in punctuation:
        string=string.replace(i,'')
    string=string.replace("\n",' ')
    list=SPLIT(string)
    return list

def Romve(lst):
    for i in range(len(lst)):
        if i==len(lst)-1:
            i=i-1
        if lst[i].data==lst[i+1].data:
            lst[i+1].data="!"
            lst[i].dataN=lst[i].dataN+lst[i+1].dataN
    for i in range(len(lst)):
        if not find(lst,"!"):
            break
        lst=popMe(lst,"!")
    return lst

def QuickSort(arr,dataType=False):
    elements=len(arr)
    if elements<2:
        return arr
    currentPosition=0
    if dataType:
        for i in range(1,elements):
            if arr[0].data>=arr[i].data:
                currentPosition+=1
                temp=arr[i]
                arr[i]=arr[currentPosition]
                arr[currentPosition]=temp
    else:
        for i in range(1,elements):
             if arr[0]<=arr[i]:
                 currentPosition+=1
                 temp=arr[i]
                 arr[i]=arr[currentPosition]
                 arr[currentPosition]=temp
    temp=arr[0]
    arr[0]=arr[currentPosition]
    arr[currentPosition]=temp
    if dataType:
        left=QuickSort(arr[0:currentPosition],True)
        right=QuickSort(arr[currentPosition+1:elements],True)
    else:
        left=QuickSort(arr[0:currentPosition])
        right=QuickSort(arr[currentPosition+1:elements])
    arr=left+[arr[currentPosition]]+right
    return arr

#------------------------------main------------------------------

lst=PrepareTheString(open("G:mf.txt","r"))

lst=QuickSort(lst,True)

for i in range(len(lst)):
    lst=Romve(lst)

lst=QuickSort(lst)

for i in range(len(lst)):
  print(lst[i])