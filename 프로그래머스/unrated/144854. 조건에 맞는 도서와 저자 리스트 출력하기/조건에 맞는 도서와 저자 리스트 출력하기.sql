select book.book_id, author.author_name, date_format(book.published_date, '%Y-%m-%d') from book book join author author
on book.author_id = author.author_id
where book.category = '경제'
order by published_date;