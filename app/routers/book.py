from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.crud import book as book_crud
from app.schemas.book import BookCreate, BookRead, BookUpdate, BookDelete
from app.database import get_db

router = APIRouter(prefix="/books", tags=["books"])

@router.get("/", response_model=list[BookRead])
def read_books(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    books = book_crud.get_books(db, skip=skip, limit=limit)
    return books

@router.post("/", response_model=BookRead)
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    return book_crud.create_book(db=db, book=book)

@router.get("/{book_id}", response_model=BookRead)
def read_book(book_id: int, db: Session = Depends(get_db)):
    db_book = book_crud.get_book(db, book_id=book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book

@router.put("/{book_id}", response_model=BookRead)
def update_book(book_id: int, book: BookUpdate, db: Session = Depends(get_db)):
    db_book = book_crud.update_book(db, book_id=book_id, book=book)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book

@router.delete("/{book_id}", response_model=BookDelete)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    db_book = book_crud.delete_book(db, book_id=book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return BookDelete(id=book_id)