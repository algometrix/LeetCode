'''
Given an array of integers A of size N and an integer B.

College library has N bags,the ith book has A[i] number of pages.

You have to allocate books to B number of students so that maximum number of pages alloted to a student is minimum.

Input 1:
    A = [12, 34, 67, 90]
    B = 2
Output 1:
    113
Explanation 1:
    There are 2 number of students. Books can be distributed in following fashion : 
        1) [12] and [34, 67, 90]
        Max number of pages is allocated to student 2 with 34 + 67 + 90 = 191 pages
        2) [12, 34] and [67, 90]
        Max number of pages is allocated to student 2 with 67 + 90 = 157 pages 
        3) [12, 34, 67] and [90]
        Max number of pages is allocated to student 1 with 12 + 34 + 67 = 113 pages

        Of the 3 cases, Option 3 has the minimum pages = 113.

Input 2:
    A = [5, 17, 100, 11]
    B = 4
Output 2:
    100

Solution Type : Binary Search of the search space
'''

def books(book_page_count, number_of_bags):
    result = []
    def req_bags(min_pages, max_pages):
        print(min_pages, max_pages)
        mid_page_count = ( min_pages + max_pages ) // 2
        if min_pages >= max_pages:
            return 0
        
        _sum = 0
        required_bags = 1
        for page in book_page_count:
            _sum += page
            if _sum > mid_page_count:
                required_bags += 1
                _sum = page
        
        if required_bags == number_of_bags:
            result.append(mid_page_count)

        if required_bags > number_of_bags:
            req_bags(mid_page_count + 1, max_pages)
        else:
            req_bags(min_pages, mid_page_count)

    number_of_books = len(book_page_count)
    if number_of_books == number_of_bags:
        return max(book_page_count)
    elif number_of_books < number_of_bags:
        return -1
    elif number_of_bags == 1:
        return sum(book_page_count)

    search_space_min = max(book_page_count)
    search_space_max = sum(book_page_count)
    req_bags(search_space_min, search_space_max)
    if len(result) == 0:
        return max(book_page_count)
    else:
        return min(result)


if __name__ == "__main__":
    A = [12, 34, 67, 90]
    B = 2
    result = books(A, B)
    print('Minimum number of max book pages : {}'.format(result))