# Notes

#### Features

1. Allow users to pay their fees by using a credit card
2. Notify users when their borrowing asset is due (via email, or sms)

#### ISBN

Each ISBN is unique to an edition of a title (paperback, hardcover) or book-like product (audiobook, ebook). For example, if a title is available in hardcover, paperback, and as an ebook and an audiobook, it will have four unique ISBNs for each edition or product.

#### Django Notes

##### Access URL paramters in Class Based Views

To access the url parameters in class based views, use self.args or self.kwargs so you would access it by doing self.kwargs['year']
