import json
import os
import re
from PIL import Image

class MLService:
    def __init__(self):
        print("ML Service initialized in fallback mode (no external APIs required)")
        
        # Common objects that might appear in photos for basic keyword matching
        self.common_objects = [
            'person', 'people', 'man', 'woman', 'child', 'baby',
            'dog', 'cat', 'bird', 'animal', 'pet',
            'car', 'truck', 'bike', 'bicycle', 'motorcycle', 'vehicle',
            'tree', 'flower', 'plant', 'garden', 'nature',
            'house', 'building', 'room', 'kitchen', 'bedroom',
            'food', 'cake', 'pizza', 'sandwich', 'drink',
            'beach', 'ocean', 'mountain', 'sky', 'cloud',
            'party', 'celebration', 'wedding', 'birthday',
            'book', 'computer', 'phone', 'laptop',
            'sunset', 'sunrise', 'night', 'day'
        ]
    
    def _analyze_filename(self, image_path):
        """Extract potential keywords from filename"""
        if not image_path:
            return []
        
        filename = os.path.basename(image_path).lower()
        # Remove extension
        filename = os.path.splitext(filename)[0]
        # Split by common separators
        words = re.findall(r'[a-zA-Z]+', filename)
        
        # Match against common objects
        detected = []
        for word in words:
            if word in self.common_objects:
                detected.append(word)
        
        return detected
    
    def _analyze_image_properties(self, image_path):
        """Basic image analysis using PIL"""
        try:
            with Image.open(image_path) as img:
                width, height = img.size
                mode = img.mode
                
                # Basic size-based assumptions
                objects = []
                
                # Large images might be landscapes
                if width > 1920 or height > 1080:
                    objects.extend(['landscape', 'nature'])
                
                # Square images might be portraits or social media
                if abs(width - height) < 100:
                    objects.extend(['portrait', 'photo'])
                
                # Very wide images might be panoramic
                if width > height * 2:
                    objects.extend(['panorama', 'landscape'])
                
                return objects
        except Exception:
            return []
    
    def generate_alt_text(self, image_path):
        """Generate fallback alternative text for an image"""
        if not os.path.exists(image_path):
            return "Image uploaded by user"
        
        try:
            # Try to get basic image info
            filename_keywords = self._analyze_filename(image_path)
            image_properties = self._analyze_image_properties(image_path)
            
            # Create a descriptive alt text based on available info
            if filename_keywords:
                main_objects = filename_keywords[:2]  # Take first 2
                if len(main_objects) == 1:
                    return f"Photo of {main_objects[0]}"
                else:
                    return f"Photo with {', '.join(main_objects)}"
            
            # Fallback based on image properties
            if 'landscape' in image_properties:
                return "Landscape photo"
            elif 'portrait' in image_properties:
                return "Portrait photo"
            else:
                return "Photo uploaded by user"
                
        except Exception as e:
            print(f"Error generating alt text: {e}")
            return "Photo uploaded by user"
    
    def detect_objects(self, image_path):
        """Detect objects using basic filename and image analysis"""
        if not os.path.exists(image_path):
            return []
        
        try:
            detected_items = []
            
            # Get keywords from filename
            filename_keywords = self._analyze_filename(image_path)
            detected_items.extend(filename_keywords)
            
            # Get basic image properties
            image_properties = self._analyze_image_properties(image_path)
            detected_items.extend(image_properties)
            
            # Add some default searchable terms
            detected_items.extend(['photo', 'image', 'picture'])
            
            # Remove duplicates and return
            return list(set(detected_items))
            
        except Exception as e:
            print(f"Error detecting objects: {e}")
            return ['photo', 'image']

# Create global instance
ml_service = MLService()