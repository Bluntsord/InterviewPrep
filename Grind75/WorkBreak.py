from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict.sort(key=lambda x: -len(x))
        self.word_dict = {k:1 for k in wordDict}
        self.s = s
        self.acc = ""
        self.processed = False

        return self.backTracking()

    def early_check(self):
        char_dict = {}
        for word in self.word_dict.keys():
            for character in word:
                if character not in char_dict:
                    char_dict[character] = 1

        for char in self.s:
            if char not in char_dict:
                return False

        return True

    def backTracking(self):
        if self.acc == self.s:
            self.processed = True
            return True

        answer = False

        if self.processed:
            return True
        elif not self.early_check():
            return False

        for key in self.word_dict.keys():
            if key == self.s[len(self.acc): len(self.acc) + len(key)]:
                self.acc += key
                answer = self.backTracking()
                self.acc = self.acc.removesuffix(key)

        return answer

    def wordBreak2(self, s: str, wordDict: List[str]) -> bool:
        self.word_dict = {k: 1 for k in wordDict}
        self.memo = {}
        self.s = s
        self.processed = False

        return self.dp("")

    def dp(self, curr_string):
        if len(curr_string) > len(self.s):
            return False
        elif len(curr_string) == len(self.s):
            if curr_string == self.s:
                self.processed = True
                return self.processed
            return False
        elif curr_string in self.memo:
            return self.memo[curr_string]
        elif self.processed:
            return True

        wish = False
        for word in self.word_dict:
            if word == self.s[len(curr_string): len(curr_string) + len(word)]:
                wish = self.dp(curr_string + word)
                self.memo[curr_string] = wish

        return wish

s = "aaaab"
wordDict = ["a","aa", "aaa", "aaaa", "b"]

s1 = "abcd"
wordDict1 = ["a","abc","b","cd"]

s2 = "applepenapple"
wordDict2 = ["apple","pen"]

s3 = "catsandog"
wordDict3 = ["cats","dog","sand","and","cat"]
solution = Solution()

s4 = "fohhemkkaecojceoaejkkoedkofhmohkcjmkggcmnami"
wordDict4 = ["kfomka","hecagbngambii","anobmnikj","c","nnkmfelneemfgcl","ah","bgomgohl",
 "lcbjbg","ebjfoiddndih","hjknoamjbfhckb","eioldlijmmla","nbekmcnakif","fgahmihodolmhbi",
 "gnjfe","hk","b","jbfgm","ecojceoaejkkoed","cemodhmbcmgl","j","gdcnjj","kolaijoicbc",
 "liibjjcini","lmbenj","eklingemgdjncaa","m","hkh","fblb","fk","nnfkfanaga","eldjml","iejn",
 "gbmjfdooeeko","jafogijka","ngnfggojmhclkjd","bfagnfclg","imkeobcdidiifbm","ogeo","gicjog",
 "cjnibenelm","ogoloc","edciifkaff","kbeeg","nebn","jdd","aeojhclmdn","dilbhl","dkk","bgmck",
 "ohgkefkadonafg","labem","fheoglj","gkcanacfjfhogjc","eglkcddd","lelelihakeh","hhjijfiodfi",
 "enehbibnhfjd","gkm","ggj","ag","hhhjogk","lllicdhihn","goakjjnk","lhbn","fhheedadamlnedh",
 "bin","cl","ggjljjjf","fdcdaobhlhgj","nijlf","i","gaemagobjfc","dg","g","jhlelodgeekj",
 "hcimohlni","fdoiohikhacgb","k","doiaigclm","bdfaoncbhfkdbjd","f","jaikbciac",
 "cjgadmfoodmba","molokllh","gfkngeebnggo","lahd","n","ehfngoc","lejfcee","kofhmoh","cgda",
 "de","kljnicikjeh","edomdbibhif","jehdkgmmofihdi","hifcjkloebel","gcghgbemjege","kobhhefbbb",
 "aaikgaolhllhlm","akg","kmmikgkhnn","dnamfhaf","mjhj","ifadcgmgjaa","acnjehgkflgkd","bjj",
 "maihjn","ojakklhl","ign","jhd","kndkhbebgh","amljjfeahcdlfdg","fnboolobch","gcclgcoaojc",
 "kfokbbkllmcd","fec","dljma","noa","cfjie","fohhemkka","bfaldajf","nbk","kmbnjoalnhki",
 "ccieabbnlhbjmj","nmacelialookal","hdlefnbmgklo","bfbblofk","doohocnadd","klmed","e",
 "hkkcmbljlojkghm","jjiadlgf","ogadjhambjikce","bglghjndlk","gackokkbhj","oofohdogb",
 "leiolllnjj","edekdnibja","gjhglilocif","ccfnfjalchc","gl","ihee","cfgccdmecem",
 "mdmcdgjelhgk","laboglchdhbk","ajmiim","cebhalkngloae","hgohednmkahdi","ddiecjnkmgbbei",
 "ajaengmcdlbk","kgg","ndchkjdn","heklaamafiomea","ehg","imelcifnhkae","hcgadilb",
 "elndjcodnhcc","nkjd","gjnfkogkjeobo","eolega","lm","jddfkfbbbhia","cddmfeckheeo",
 "bfnmaalmjdb","fbcg","ko","mojfj","kk","bbljjnnikdhg","l","calbc","mkekn","ejlhdk",
 "hkebdiebecf","emhelbbda","mlba","ckjmih","odfacclfl","lgfjjbgookmnoe","begnkogf",
 "gakojeblk","bfflcmdko","cfdclljcg","ho","fo","acmi","oemknmffgcio","mlkhk",
 "kfhkndmdojhidg","ckfcibmnikn","dgoecamdliaeeoa","ocealkbbec","kbmmihb","ncikad",
 "hi","nccjbnldneijc","hgiccigeehmdl","dlfmjhmioa","kmff","gfhkd","okiamg","ekdbamm",
 "fc","neg","cfmo","ccgahikbbl","khhoc","elbg","cbghbacjbfm","jkagbmfgemjfg",
 "ijceidhhajmja","imibemhdg","ja","idkfd","ndogdkjjkf","fhic","ooajkki","fdnjhh",
 "ba","jdlnidngkfffbmi","jddjfnnjoidcnm","kghljjikbacd","idllbbn","d","mgkajbnjedeiee",
 "fbllleanknmoomb","lom","kofjmmjm","mcdlbglonin","gcnboanh","fggii","fdkbmic","bbiln",
 "cdjcjhonjgiagkb","kooenbeoongcle","cecnlfbaanckdkj","fejlmog","fanekdneoaammb",
 "maojbcegdamn","bcmanmjdeabdo","amloj","adgoej","jh","fhf","cogdljlgek","o",
 "joeiajlioggj","oncal","lbgg","elainnbffk","hbdi","femcanllndoh","ke","hmib",
 "nagfahhljh","ibifdlfeechcbal","knec","oegfcghlgalcnno","abiefmjldmln","mlfglgni",
 "jkofhjeb","ifjbneblfldjel","nahhcimkjhjgb","cdgkbn","nnklfbeecgedie","gmllmjbodhgllc",
 "hogollongjo","fmoinacebll","fkngbganmh","jgdblmhlmfij","fkkdjknahamcfb","aieakdokibj",
 "hddlcdiailhd","iajhmg","jenocgo","embdib","dghbmljjogka","bahcggjgmlf","fb","jldkcfom",
 "mfi","kdkke","odhbl","jin","kcjmkggcmnami","kofig","bid","ohnohi","fcbojdgoaoa","dj",
 "ifkbmbod","dhdedohlghk","nmkeakohicfdjf","ahbifnnoaldgbj","egldeibiinoac","iehfhjjjmil",
 "bmeimi","ombngooicknel","lfdkngobmik","ifjcjkfnmgjcnmi","fmf","aoeaa","an",
 "ffgddcjblehhggo","hijfdcchdilcl","hacbaamkhblnkk","najefebghcbkjfl","hcnnlogjfmmjcma",
 "njgcogemlnohl","ihejh","ej","ofn","ggcklj","omah","hg","obk","giig","cklna",
 "lihaiollfnem","ionlnlhjckf","cfdlijnmgjoebl",
 "dloehimen","acggkacahfhkdne","iecd","gn","odgbnalk","ahfhcd","dghlag","bchfe",
 "dldblmnbifnmlo","cffhbijal","dbddifnojfibha","mhh","cjjol","fed","bhcnf","ciiibbedklnnk",
 "ikniooicmm","ejf","ammeennkcdgbjco","jmhmd","cek","bjbhcmda","kfjmhbf","chjmmnea","ifccifn",
 "naedmco","iohchafbega","kjejfhbco","anlhhhhg"]


input = [[s, wordDict], [s1, wordDict1], [s2, wordDict2], [s3, wordDict3]]
output = [True, True, True, False]
zipped = zip(input, output)

answer = True
# for input, output in zipped:
#     temp = solution.wordBreak2(input[0], input[1]) == output
#     answer &= temp

# print(answer)

print(solution.wordBreak2(s4, wordDict4))