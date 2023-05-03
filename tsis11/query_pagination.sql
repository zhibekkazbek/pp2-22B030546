CREATE FUNCTION query_pagination(page_size INTEGER, page_number INTEGER) RETURNS TABLE (
    name VARCHAR(20),
    number VARCHAR(20)
) AS $$
BEGIN
    RETURN QUERY
        SELECT  book.name, book.number
        FROM book
        ORDER BY book.name
        LIMIT page_size
        OFFSET (page_number - 1) * page_size;
END;
$$ LANGUAGE 'plpgsql';