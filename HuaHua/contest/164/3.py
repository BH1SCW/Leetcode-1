from __future__ import annotations
import string
class Trie():
    def __init__(self):
        self.trie = {}

    def add(self, word):
        trie = self.trie
        for w in word:
            trie = trie.setdefault(w, {})
        trie['*'] = {}

    def get_prefix(self, prefix, k):
        trie = self.trie
        for w in prefix:
            trie = trie.get(w, {})
        def helper(prefix, k, trie, ans):
            if len(ans) == k or not trie: return
            if '*' in trie:
                ans.append(prefix)
            for c in string.ascii_lowercase:
                helper(prefix + c, k, trie.get(c, {}), ans)
        ans = []
        helper(prefix, k, trie, ans)
        return ans

import bisect
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products = sorted(products)
        ans = []
        for i, c in enumerate(searchWord):
            prefix = searchWord[:i + 1]
            i = bisect.bisect_left(products, prefix)
            ans.append([w for w in products[min(len(products), i + 1) : min(i + 4, len(products))] if w.startswith(prefix)])
        return ans

    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        for p in products:
            trie.add(p)
        ans = []
        for i in range(len(searchWord)):
            ans.append(trie.get_prefix(searchWord[:i + 1], 3))
        return ans


if __name__ == '__main__':
    sol = Solution()
    products = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
    searchWord = "mouse"
    print(sol.suggestedProducts(products, searchWord))
    products = ["havana"]
    searchWord = "havana"
    print(sol.suggestedProducts(products, searchWord))
    products = ["bags", "baggage", "banner", "box", "cloths"]
    searchWord = "bags"
    print(sol.suggestedProducts(products, searchWord))
    products = ["havana"]
    searchWord = "tatiana"
    print(sol.suggestedProducts(products, searchWord))
    products = ["eucgsmpsyndddijvpxfagngnjbzxuajxmrmszwtjvwswgdrojt","mervtkzsouapfbky","eucgsmpsyndddijvpxfagngnjbzxuajxnzjk","eduvadjohhskmyzipulgjeat","eucgsnatcadpbcyrxlgldpcaijmnojdkjqfwxkz","eucgsmpsynevhpeoqwbgdidv","yvu","eucgsmpsyndddijvpxfagnbjthdmywjcmbmgpfrvwhdarjske","eixctybvrnuyqibnpxpbcpcqcq","eucgsmpsyndddijvpxfagngnjrcnbbwae","lrvlimn","eucgsmpsyndddijvpxfagngnjbzgsidschcqhm","thhnadanjkbrcnofgpdfthvcodrmrezulkuytrqosqaooecqom","eucgsmpsyndddijvpxfagngwcpixbrkupusfqoyihroghoae","eucgsmpsyndddijvpxmmydswjxsdmer","fhfhindvjohibmsoipvdyedlxoinlumjlb","lsuinsmrgxxhswxshvogzxojsbvhzbcioldypag","ptbyxfktngjsofvicpvsmyqddacyahf","yjhiemwpwfpyewvcfbtljsrwlfiihwisqekfoearodlvhoejq","atoygkvdbdvmuukgfjnufsnhjcsaxk","eucgsdwqeaslgrthiruatrpulqyjgmsbdljebf","eucgsmpsyndddijvpxpcyrilzawoid","eucgsmpsyndddijvpxfagngnjbhvxvjmecfdqzpokhzpqdo","faoywdrvlgacdcfj","eucgsmpsynddwdgwnssfvds","eucgsmpsyndqgjneynofkuebob","asafyzzpxlltqyscywuahwinwijuccwnd","eucgsmpsyndddiznbxfvpqei","eucgsmpsyndddijvpximqtdtlybvziqhdvowuijbkurk","hvxmdjutynhrxyubizbyjwwxfpvblzxvfrca","eucgsu","jhckeuhdvbfdzmyjbjcfariwejezwhtzojeyhxjwegqgrl","eucgsmpsyndddijvpxfagngnjsjjbob","eucgsmpsyndddijvpxfdtbeujjoeqvezdjmopfcmzohuantaid","eucgsmpsyndddijvpxfagngnjbzxuajxmrmszloha","eucgsmpsyndddijvpxfagngnjbzxuajlkwhlwhuwmyagdvymu","jdskdhwkehgqazzweqyzmqzsikjnwgylnhgugjixyrpmyrs","eucgsmpsdney","sasmjvaqjrrovkxqccfpqyruscxgzkbeekz","eucgsmpsyndddijvpxfagngnjbzxuajxmrmszwtjjofldab","eucgsmpsyndddijvpxfagngnjbzxuajxmrmszwtjvwswgdros","ekszgjqykwcwatzrzykatpxcasaifohwrrhipm","shfcpdjhktwfcqezsabkzyzyuibxpzxggnxgcwflloucbgodpm","tpcxhiehypiqtaxzdjxhofufucblqvkoqhlgxgozolaelf","swtrepxomxqemgodrupgigvpxxgptmilfkmzhfnr","dcvzdk","eucgsmpsyndddijvpxfagngnjbzxuajxmrmssckqdpjjasnms","nknhhv","eucgsmpsyndddijvpxfagngnjbzxuajxmrmszwtjvwjyi","qrsqrmqtpajtewxiegcevy","eucgsmpsyndddijvpxfagnfqcq","eucgsmpsyndddijvpxfagngnjbzxuajxmicjxmxhnrxbbczh","eucgshcaieewetzvzwigqfrlwpy","ogubeczu","eucgsmpsyndddijvpxfagngnjbzxuavqyzgaeyi","eucgsmpsyndddijvpxfagngnjbzxuajxmonbleriwyuvlnsfzt","jhz","eucgsmpsyndddijvpxfagngnjbzxuajxmrmszwtjvwswgdroje","xasvjrkqyxory","eucgsmpsyndddijvpxfagngnjbzxuajxmrmszwtjvwsehufy","eucgsmpsyndntjxkzpjstoke","eucgsmpsyndddijvpxfagngnjbzxuajxmrmszhwsbfrppvadx","eucgsmrczev","eucgsmpsyndddijvpxfagngnjbzxuafelaasrnq","eucgsmpsyndddijvpxohsjopdnlnlhksjadjvuvroybu","gnntehraxahinoyqdrspmjaunucrzw","roqdenkakwsbkcbkijyrpfdehrfj","eucgsmpsyndddijvpxfagngnjbzxuajxmrmszwtjvwswgusf","eucgsmpsyndddijvpxfagngnjbjkffxzscalu","eugyortzihuywhfyrwubdfuomvcjudxtappednlohmxz","eucgsmpsyndddijvpxfagngnjbzxuajxmrmszwtjvwswq","eucjqsqvatpjbfvhowkaagxyidiyymapdumaxgoqgbpwsu","eucgsmpsyndddijvpxfagngnjbzxuajxmrmszwtjvwswgdrk","es","eucgsmpsyndddijvpxfagngnjbzxuajxmrmszwtjvwswgdwv","kbninamhdqpoyzznnsqxzmieqajsqrjocrqbmfhwomstdc","jbwggbwtybranddatuybnzre","ludoupnbvsxksvmtaxuuiymidzotziwbqaclvvk","eucgsmpsyndddijvpxfagngnsgpnllzgpyirgem","eucgsmpsyndddijvpxfagngnjbzxuajxmrmszwtebvruvqmpx","nwbqryotfdaopywffjbikuqzraabwngcicsufkeerbpnfyi","eucgsmpsyndddijvoaevblhxotmowpxwpuhzmemw","eucgsmpsyndddijvpxfagngnjbzxuajxmrmszwtjvwswgu","eucgsmpsyndddijvpcfjbzthtculbzszzfaroncw","grygljuxydgpoygjoemajbkaqmbwyverlruejnigqdsvdpwm","eucgsmpsyomtefhlwqluqgcckz","eucijltqylixpvjwtlhurqdseysduhivw","eucgsmpsyndddijvpxfagngnjbzxuajxmrbcm","zibchozkzyhdsmfcryjyzkzgyohjs","yiuxtmtzrnnitnpzyfgfctnlednanfwtjplvueab","eucgsmpsyndddijvpxfagngnjbzxuajxmrmszwtjvwslgknojn","eucgsmpsyndddijvpxfagngnjbxzehobuljrngufbcks","bwbbmbvwzegxmqhdmufnvwpwtykmdvwngqtdwym","eucgsmpsyndddijvpxfagnoezpyieslubwxeobrnktvnpinamb","eucgsmpslmkdakhg","eucgsmczlqunsmfbrodtrtevmuflaf","rpofbqaryrhmqzqkzrmhhsmtgfecva","pmvfbplrjqcmxlpypswxgqemjpxmwmswesrhwmicumoilapzhy","eucgsmpsyndddezzokejvhvdmsoaaoowwottmw","rmvmikeynztayityavakrt","tdeypjrxduem","fqvsmpnzkzuubhuwchdqy","eucgsmpsyoesekvyqvtmymaplhzynaupevoihscjkrjtcj","eucgsmpsyndddijvpxfagngnjbzxjh","jghjdzajfpvyesz","eucgsmpsyndddijvpxfagngnjbzxlmymsyqvaojj","eucgsmpsyndddijvpxfagngnjbzxuajxmrmszwdetn","eunahmcfpnnjavmduowjntsgo","eucgsmpsyndddijvpxfagngnjbzqinqttopi","ubgzjxnomgcnrbbhyppemgyejbycpgamympgupaetudz","mtuindengcxqg","eucgdxsvzyxpbwtnqmzundoosvddromqhydyyjich","eucgsmpsyndddijvpxfagngnjbzxuajxmrmszwtjvwswgkqoyw","eucgsmpsyndddijvpxfagngnjbzxuajxmrmszwtjvwswgdrog","eucgsmpsyndddijvpxfagnpcl","eucgsmpsyndddijvpxfagngnjbzjegcxjcrslyvgbd","nhb","eucgsmpsyndddijvpxfagngnjbzxuajxmrmszwtjvwsudaj","vnyfkvdguu","eucshaijqdl","eucgsmpsyndddijvpxfagngnjbzxuyxowpbndxvxayzxfp","fvgk","eucgsmpslzukdhnbtmsycj","wvpelpocfsodafurhbgbytnta","eucgsmpsyndddijvpxfagngnjbzzetehbbepo","eucgsmpsyndddijvpxfagngnjbzxuajxmrmszwtjvwswgdayg","eucgsmpsyndddijvpxfagngnjbzxuajxjtkkz","knhrz","eucgsmpsyndddijvpxfagngnjbzxuyretdzgzkqaep","eucgsmpsyndddijvpxfagngnjbzxuajxmgi","eucgdjnclcqogrzxi","clliyxtdxzwwz","eucgsmpsyndddijvpxfagngnjbzxuajxmrmszwtjvvev","sugaphcopoyjzoxdpznrkrgjzcfdddvcktwxukcnan","eucgsmpsyndddijvpxfagngnjbzxuajxmrmszwtjvwswgdrojp","vwavfxqerifzseyfefbchueoadvcoximlvowsndrwxspqsn","ejafexrgcikuqefkvlfe","eucgsmpsyndddijvpxfaiuejxgpzbirbus","eucgsmpsyndddijvpxfagngnjbzzdo","bgtdtziavmvfbkexrmqzojkdrapfbljxghlesmflzvgxrooc","eucgsmpsyndddijvpxfagludvrubjhfhn","jsposqsidurgsqjwkabv","eucgsmpsyndddijvpxfagnplbcjevfnfaezqcijiixrrcd","wdhaxpoe","nkj","eucgsmpsyndddijvpxfagngnjbzxuajxmweazgncksq","eucgsmpsyndddijvpxfagnyxks","bouogc","eucgabxhtbnohgmunhrospjzqozczhowc","udcilqgipfjswuscpxtbgqancfolgqbvfvrzsy","eucgsmpsyndddijvpcdswmsvlekrtarkybjwovevieve","zkwfbyawpokgpnzzikaybfosdbqjmkdthsyoojb","gabgl","bkyxlqjgdsuhzbpvtnaobudwsrjqvceliadetviiar","eucgsmpsyndddijvpxfagngnjbzxuajxqqdlwpeyxgtuvbfqj","eucgsmpsyndddijvpxfagngnjbzxuajxmrmszwtjvwswwvy","ryxcr","eucgsmpsyndddijvpxfagngnjbzvrkbgrrtcpbqvlktqwwxxn","eucgsmpsyndddijfagrxzrdg","eucgsmhsnicnajhcaca","revsyodsujynljmd","fficqqokrlkfwsbosapqvaurdk","eucgudniqtxzmtschgm","eucgsmpsyncxbvicmuafacp","eucgsmpsyndddijvpxfagngnjbzxuajxmrmszwtjvwswgjrp","qvjbtmibwikrugaeihweuumhajcffcurgn","eucgsmpsyndddijvpxfagngnjbzxuajxmrmszwtjvwswgdcum","jolquz","eucgsmpsyndddijvpxfagngnjbzxuajxmrmszwtjyfpyyv","eucgsmpsyndddijvpxfagngnjbzxubimdvzlcpv","mesisdbvntasidlsnpbyrv","aekcjkuqrjfujvztrpiksbkegngbilgshwdgmfxz","fcmragokrxletuojnwflovikmovutvdzomlwyidpbzu","eucgsmpsynyozqjvjgnqtgxktlorcaij","eucgsqszvinjizxxvhypkfcigp","pxrai","eucgsmpsyndddijvpxfagngnjbzxuajxmrmszwtjvwswgdnzxa","eucgsmpsyndddijvpxfagngnjbzxuajxmrmszwtjvnannjxw","eucgsmpsyndddijvpxfagngnjbzxuajxmrmszwtjvwswgdrodu","kycywphmwwyeag","truu","eucgsmpsynajtisffvgqgafmdojgethmlygcekgrysvy","eucgsmpsyndddijvpxfagngnjbzxuajolf","eucgsmpsyndddijvvdpeqcwgnveozoyehjsul","eucgsmpsyndddijvsnsgoumnhjvhklzazpoqgfayum","dgnqyhduqwjunvwqkteoquyxmhi","ourbrwsthwtrfzgakvzxppbihjpsogitmoswlxalzlggzxtay","eucgsmpsyndddibedezerylnt","eucgsmpsyndddijvpxvzbiv","eucgsmpsynwdxxmogfmvuql","eucgsmpsywmnftesxvxklkezbkqbiitesnrjebsspij","eucgsbvboupistecce","iimgotnjnpwsmgqekkdtzfozjdv","eucgsmpsyndddijvpxfaxegyotcospqgyxenjferjjunmzsidt","eucgsmpsyndddijvpxfagngnjbzxuajxmvbnjxougpcblekprx","csdpcsaacavnznbqwiqlcsjzrdl","eucgsmpplakpuykrqty","eucgsmpsyndddijvpxfagngnjbzxuajxmrmszwtjvwswgdroje"]
    searchWord = "eucgsmpsyndddijvpxfagngnjbzxuajxmrmszwtjvwswgdrojjseclfhpnsjtqdqfhapmkmfqmzaunfhvkcbeqhowuuerztwldxaegwkghzthoauesdmbshzxlnpagcnyyicmtbhoqrkopemdacrkhdsxoosfhoaokqspqndtieukzjbkqixinrtqrzblufhucpzomvpmcvzfuebjfkywangcqutpzrwkwolpxuqfyjdwwrnhvnzkorsiklgqmwijynmrfezlpmdkkhafyxumiyqxhxbmxzmmcmxkajvwohhjqfuqlvknrqbjsnoimxwzbhlbddbzlwqbjpgwvjgvhgubmabuomjdmqouarvjuqzyvmsnmjaqzdmtwhaelglbt"
    print(sol.suggestedProducts(products, searchWord))

