

query {
  # Note that fields names become camelcased
  booksByUser(ownedBy: 1) {
    title
  } 

}



query {
  # Note that fields names become camelcased
  searchBooks(query: "test" ) {
    title
  } 

}


