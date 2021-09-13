resource "aws_s3_bucket" "b" {
  bucket = "${var.website_bucket_name}"
  acl    = "private"

  tags = {
    Name        = "${var.website_bucket_name}"
    Environment = "Dev"
  }
}