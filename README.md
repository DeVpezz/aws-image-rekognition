<h1>🧠 Image Label Generator using AWS Rekognition</h1>

<p>
This project is a <strong>fully serverless, cloud-based web application</strong> that allows users to upload images 
and automatically detect objects and scenes using <strong>Amazon Rekognition</strong>.
The detected labels are stored in <strong>Amazon DynamoDB</strong> and displayed on a simple web interface.
</p>

<hr>

<div class="section">
<h2>📌 What is This Project?</h2>

<p>
The Image Label Generator is a web application where:
</p>

<ul>
    <li>A user uploads an image from a browser</li>
    <li>AWS analyzes the image using AI</li>
    <li>Detected objects (like car, person, animal, etc.) are returned</li>
    <li>The results are stored and displayed to the user</li>
</ul>

<p>
The entire application runs without managing any servers, making it highly scalable, secure, and cost-efficient.
</p>
</div>

<hr>

<div class="section">
<h2>🎯 Why This Project?</h2>

<p>
This project was built to understand and demonstrate:
</p>

<ul>
    <li>How real-world <strong>serverless architectures</strong> work</li>
    <li>Secure image uploads using <strong>pre-signed URLs</strong></li>
    <li>Integration of <strong>AI services</strong> without managing ML models</li>
    <li>Event-driven processing using AWS</li>
    <li>How multiple AWS services communicate securely</li>
</ul>

<div class="highlight">
<strong>Why it matters:</strong>  
This project reflects real production use cases such as content moderation, image classification, and automated tagging systems.
</div>
</div>

<hr>

<div class="section">
<h2>🛠️ AWS Services Used</h2>

<ul>
    <li><strong>Amazon S3</strong> – Image storage and static website hosting</li>
    <li><strong>AWS Lambda</strong> – Serverless backend logic</li>
    <li><strong>Amazon Rekognition</strong> – AI-powered image analysis</li>
    <li><strong>Amazon DynamoDB</strong> – NoSQL database for storing labels</li>
    <li><strong>Amazon API Gateway</strong> – REST APIs for frontend communication</li>
    <li><strong>AWS IAM</strong> – Secure permissions and role-based access</li>
    <li><strong>Amazon CloudWatch</strong> – Logs and monitoring</li>
</ul>
</div>

<hr>

<div class="section">
<h2>⚙️ How This Project Works (Architecture)</h2>

<p>
The project follows an <strong>event-driven serverless architecture</strong>:
</p>

<ol>
    <li>User uploads an image from the web UI</li>
    <li>Frontend requests a pre-signed upload URL from API Gateway</li>
    <li>Lambda generates a secure, time-limited S3 upload URL</li>
    <li>Browser uploads the image directly to S3</li>
    <li>S3 triggers a Lambda function automatically</li>
    <li>Lambda calls Amazon Rekognition to detect labels</li>
    <li>Detected labels are stored in DynamoDB</li>
    <li>Frontend polls another API to fetch and display labels</li>
</ol>
</div>

<hr>

<div class="section">
<h2>🔐 Security Design</h2>

<ul>
    <li>No AWS credentials exposed on frontend</li>
    <li>Uploads handled via <strong>temporary pre-signed URLs</strong></li>
    <li>IAM roles follow <strong>least privilege principle</strong></li>
    <li>S3 bucket remains private</li>
    <li>API Gateway controls access to Lambda</li>
</ul>
</div>

<hr>

<div class="section">
<h2>📂 Project Structure</h2>

<pre>
project-root/
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── lambda/
│   ├── generate-upload-url.py
│   ├── image-label-generator.py
│   └── get-image-labels.py
│
└── README.html
</pre>
</div>

<hr>

<div class="section">
<h2>🧪 Example Output</h2>

<pre>
{
  "imageName": "uuid-car.jpeg",
  "labels": [
    { "Name": "Car", "Confidence": 99.2 },
    { "Name": "Vehicle", "Confidence": 98.5 },
    { "Name": "Road", "Confidence": 96.1 }
  ]
}
</pre>
</div>

<hr>

<div class="section">
<h2>📈 How This Project is Helpful</h2>

<ul>
    <li>Demonstrates real AWS production workflows</li>
    <li>Useful for learning serverless architecture</li>
    <li>Applicable to content moderation and tagging systems</li>
    <li>Resume-ready cloud project</li>
    <li>Scales automatically with usage</li>
</ul>
</div>

<hr>

<div class="section">
<h2>🧠 Key Learnings</h2>

<ul>
    <li>Working with pre-signed URLs securely</li>
    <li>Debugging IAM and permission issues</li>
    <li>Handling asynchronous workflows</li>
    <li>Integrating AI services without ML knowledge</li>
    <li>Designing cost-efficient cloud solutions</li>
</ul>
</div>

<hr>

<div class="section">
<h2>🚀 Future Enhancements</h2>

<ul>
    <li>React-based frontend</li>
    <li>User authentication (Amazon Cognito)</li>
    <li>CloudFront distribution</li>
    <li>Image preview and history</li>
    <li>Search and filtering of labels</li>
</ul>
</div>

<hr>

<div class="section">
<h2>👤 Author</h2>

<p>
<strong>Siddharth Singh</strong><br>
Aspiring Cloud / DevOps Engineer<br>
India
</p>
</div>

<hr>

<p><strong>⭐ If you like this project, give it a star on GitHub!</strong></p>

</body>
</html>
