#Scraping config

TERMS_TO_LOOK_FOR = ["nowa droga","nową drogę", "nowej drogi", "wytyczył", "przejście", "OS", "powtórzenie",
                    "powtórzenia", "wyciągi", "wyciąg", '8b', "8c", "9a", "9b", "stylu alpejskim"]

# Blog config

CREDENTIALS = '' # Put path to your client secret here
BLOG_ID = "xxxxxxxxxxxxxxxxxxxxxxxx"
SCOPES = ['https://www.googleapis.com/auth/blogger', 'https://www.googleapis.com/auth/drive.file']

POST_OBJECT = {
  "author": { # The author of this Post.
    "displayName": "A String", # The display name.
    "id": "A String", # The identifier of the creator.
    "image": { # The creator's avatar.
      "url": "A String", # The creator's avatar URL.
    },
    "url": "A String", # The URL of the creator's Profile page.
  },
  "blog": { # Data about the blog containing this Post.
    "id": "A String", # The identifier of the Blog that contains this Post.
  },
  "content": "A String", # The content of the Post. May contain HTML markup.
  "customMetaData": "A String", # The JSON meta-data for the Post.
  "etag": "A String", # Etag of the resource.
  "id": "A String", # The identifier of this Post.
  "images": [ # Display image for the Post.
    {
      "url": "A String",
    },
  ],
  "kind": "A String", # The kind of this entity. Always blogger#post.
  "labels": [ # The list of labels this Post was tagged with.
    "A String",
  ],
  "location": { # The location for geotagged posts.
    "lat": 3.14, # Location's latitude.
    "lng": 3.14, # Location's longitude.
    "name": "A String", # Location name.
    "span": "A String", # Location's viewport span. Can be used when rendering a map preview.
  },
  "published": "A String", # RFC 3339 date-time when this Post was published.
  "readerComments": "A String", # Comment control and display setting for readers of this post.
  "replies": { # The container of comments on this Post.
    "items": [ # The List of Comments for this Post.
      {
        "author": { # The author of this Comment.
          "displayName": "A String", # The display name.
          "id": "A String", # The identifier of the creator.
          "image": { # The creator's avatar.
            "url": "A String", # The creator's avatar URL.
          },
          "url": "A String", # The URL of the creator's Profile page.
        },
        "blog": { # Data about the blog containing this comment.
          "id": "A String", # The identifier of the blog containing this comment.
        },
        "content": "A String", # The actual content of the comment. May include HTML markup.
        "id": "A String", # The identifier for this resource.
        "inReplyTo": { # Data about the comment this is in reply to.
          "id": "A String", # The identified of the parent of this comment.
        },
        "kind": "A String", # The kind of this entry. Always blogger#comment.
        "post": { # Data about the post containing this comment.
          "id": "A String", # The identifier of the post containing this comment.
        },
        "published": "A String", # RFC 3339 date-time when this comment was published.
        "selfLink": "A String", # The API REST URL to fetch this resource from.
        "status": "A String", # The status of the comment (only populated for admin users).
        "updated": "A String", # RFC 3339 date-time when this comment was last updated.
      },
    ],
    "selfLink": "A String", # The URL of the comments on this post.
    "totalItems": "A String", # The count of comments on this post.
  },
  "selfLink": "A String", # The API REST URL to fetch this resource from.
  "status": "A String", # Status of the post. Only set for admin-level requests.
  "title": "A String", # The title of the Post.
  "titleLink": "A String", # The title link URL, similar to atom's related link.
  "updated": "A String", # RFC 3339 date-time when this Post was last updated.
  "url": "A String", # The URL where this Post is displayed.
}