class SocialMediaProfile:
    def __init__(self, username):
        self.username = username
        self.posts = []

    def add_post(self, content):
        self.posts.append(content)
        print(f"{self.username} added a new post: {content}")

    def display_timeline(self):
        print(f'timeline : {self.username}')
        for i, post in enumerate(self.posts, start= 1):
            print(f'{i}:{post}')


def main():
    profile = SocialMediaProfile('johndoe')

    profile.add_post('Hello world')
    profile.add_post('Had a great day')
    profile.add_post('Wasssup')

    profile.display_timeline()

if __name__ == '__main__':
    main()