#!/usr/bin/env python3
"""
Website File Cleanup & Compression Script
Kitchener-Waterloo Wizards Basketball Association

This script will:
1. Identify essential production files vs backups/duplicates
2. Create compressed archives of backup files
3. Remove redundant files
4. Organize the site into a clean structure
"""

import os
import shutil
import tarfile
import gzip
import glob
from datetime import datetime

class WebsiteCleanup:
    def __init__(self):
        self.essential_files = [
            # Core HTML pages
            'index.html',
            'registration.html', 
            'about.html',
            'rep-teams.html',
            'development.html',
            'individual-training.html',
            'upcoming-events.html',
            'photo-gallery.html',
            'sitemap.html',
            'u11-rep-tryouts-flyer.html',
            
            # Essential assets
            'favicon.ico',
            'CNAME',
            
            # Keep only the best mobile optimization files
            'mobile-ultra.css',
            'mobile-ultra.js',
            'critical-mobile.css',
            
            # Images (if any exist in root)
        ]
        
        self.backup_patterns = [
            '*.original.html',
            '*.backup',
            '*.bak',
            '*-backup',
            '*.star-backup',
            '*.ios-backup', 
            '*.touch-backup',
            '*.timeout-backup',
            '*.timeout-bak',
            '*.gz',
        ]
        
        self.development_files = [
            'index-mobile-optimized.html',
            'index-smooth-mobile.html',
            'index-ultra-mobile.html',
            'test-mobile-performance.html',
            
            # Development CSS/JS files (keep only the best ones)
            'mobile-smooth.css',
            'mobile-scroll-ultimate.css',
            'mobile-optimization-template.css',
            'minimal-icons.css',
            'deferred-styles.css',
            
            'mobile-performance-fix.js',
            'mobile-scroll-ultimate.js', 
            'mobile-smooth.js',
            'deferred.js',
            'verify_final_seo.js',
        ]
        
        self.script_files = [
            '*.py',
            'comprehensive-bug-check.py',
        ]
        
        self.documentation_files = [
            '*.md',
        ]
        
        self.files_moved = 0
        self.files_compressed = 0
        self.space_saved = 0
        
    def get_file_size(self, filepath):
        """Get file size in bytes"""
        try:
            return os.path.getsize(filepath)
        except:
            return 0
    
    def create_archive_directory(self):
        """Create directory for archived files"""
        archive_dir = "archived-files"
        if not os.path.exists(archive_dir):
            os.makedirs(archive_dir)
            print(f"✅ Created archive directory: {archive_dir}/")
        return archive_dir
    
    def create_backup_archive(self):
        """Create compressed archive of all backup files"""
        print("\n📦 Creating backup archive...")
        archive_dir = self.create_archive_directory()
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_archive = f"{archive_dir}/backups_{timestamp}.tar.gz"
        
        backup_files = []
        for pattern in self.backup_patterns:
            backup_files.extend(glob.glob(pattern))
        
        if backup_files:
            with tarfile.open(backup_archive, 'w:gz') as tar:
                for file in backup_files:
                    if os.path.exists(file):
                        file_size = self.get_file_size(file)
                        tar.add(file)
                        self.space_saved += file_size
                        self.files_compressed += 1
                        print(f"  📄 Archived: {file}")
            
            print(f"✅ Created backup archive: {backup_archive}")
            
            # Remove original backup files
            for file in backup_files:
                if os.path.exists(file):
                    os.remove(file)
                    print(f"  🗑️  Removed: {file}")
        else:
            print("ℹ️  No backup files found to archive")
    
    def create_development_archive(self):
        """Create compressed archive of development files"""
        print("\n🔧 Creating development files archive...")
        archive_dir = self.create_archive_directory()
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        dev_archive = f"{archive_dir}/development_{timestamp}.tar.gz"
        
        dev_files = []
        for file in self.development_files:
            if os.path.exists(file):
                dev_files.append(file)
        
        if dev_files:
            with tarfile.open(dev_archive, 'w:gz') as tar:
                for file in dev_files:
                    file_size = self.get_file_size(file)
                    tar.add(file)
                    self.space_saved += file_size
                    self.files_compressed += 1
                    print(f"  📄 Archived: {file}")
            
            print(f"✅ Created development archive: {dev_archive}")
            
            # Remove original development files
            for file in dev_files:
                if os.path.exists(file):
                    os.remove(file)
                    print(f"  🗑️  Removed: {file}")
        else:
            print("ℹ️  No development files found to archive")
    
    def create_scripts_archive(self):
        """Create archive of Python scripts"""
        print("\n🐍 Creating scripts archive...")
        archive_dir = self.create_archive_directory()
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        scripts_archive = f"{archive_dir}/scripts_{timestamp}.tar.gz"
        
        script_files = []
        for pattern in self.script_files:
            script_files.extend(glob.glob(pattern))
        
        # Remove this cleanup script from the list (keep it active)
        script_files = [f for f in script_files if not f.endswith('website-cleanup.py')]
        
        if script_files:
            with tarfile.open(scripts_archive, 'w:gz') as tar:
                for file in script_files:
                    if os.path.exists(file):
                        file_size = self.get_file_size(file)
                        tar.add(file)
                        self.space_saved += file_size
                        self.files_compressed += 1
                        print(f"  📄 Archived: {file}")
            
            print(f"✅ Created scripts archive: {scripts_archive}")
            
            # Remove original script files
            for file in script_files:
                if os.path.exists(file):
                    os.remove(file)
                    print(f"  🗑️  Removed: {file}")
        else:
            print("ℹ️  No script files found to archive")
    
    def create_documentation_archive(self):
        """Archive documentation files"""
        print("\n📚 Creating documentation archive...")
        archive_dir = self.create_archive_directory()
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        docs_archive = f"{archive_dir}/documentation_{timestamp}.tar.gz"
        
        doc_files = []
        for pattern in self.documentation_files:
            doc_files.extend(glob.glob(pattern))
        
        if doc_files:
            with tarfile.open(docs_archive, 'w:gz') as tar:
                for file in doc_files:
                    if os.path.exists(file):
                        file_size = self.get_file_size(file)
                        tar.add(file)
                        self.space_saved += file_size
                        self.files_compressed += 1
                        print(f"  📄 Archived: {file}")
            
            print(f"✅ Created documentation archive: {docs_archive}")
            
            # Remove original documentation files
            for file in doc_files:
                if os.path.exists(file):
                    os.remove(file)
                    print(f"  🗑️  Removed: {file}")
        else:
            print("ℹ️  No documentation files found to archive")
    
    def remove_system_files(self):
        """Remove system files like .DS_Store"""
        print("\n🧹 Removing system files...")
        
        system_files = ['.DS_Store', 'Thumbs.db', '._.DS_Store']
        
        for file in system_files:
            if os.path.exists(file):
                os.remove(file)
                print(f"  🗑️  Removed: {file}")
    
    def list_remaining_files(self):
        """List files remaining after cleanup"""
        print("\n📋 Files remaining after cleanup:")
        
        all_files = []
        for pattern in ['*.html', '*.css', '*.js', '*.ico', 'CNAME']:
            all_files.extend(glob.glob(pattern))
        
        # Also check for directories
        for item in os.listdir('.'):
            if os.path.isdir(item):
                all_files.append(f"{item}/")
        
        all_files.sort()
        
        for file in all_files:
            if os.path.isdir(file.rstrip('/')):
                print(f"  📁 {file}")
            else:
                size = self.get_file_size(file) / 1024  # KB
                print(f"  📄 {file} ({size:.1f} KB)")
    
    def run_cleanup(self):
        """Run the complete cleanup process"""
        print("🧹 WEBSITE CLEANUP & COMPRESSION")
        print("=" * 50)
        print("🏀 Kitchener-Waterloo Wizards Basketball Association")
        print("=" * 50)
        
        # Calculate initial directory size
        initial_files = len([f for f in os.listdir('.') if os.path.isfile(f)])
        
        print(f"\n📊 Initial state: {initial_files} files")
        
        # Run cleanup steps
        self.create_backup_archive()
        self.create_development_archive() 
        self.create_scripts_archive()
        self.create_documentation_archive()
        self.remove_system_files()
        
        # Final report
        final_files = len([f for f in os.listdir('.') if os.path.isfile(f)])
        space_saved_mb = self.space_saved / (1024 * 1024)
        
        print("\n" + "=" * 50)
        print("🎯 CLEANUP COMPLETE!")
        print("=" * 50)
        print(f"📊 Files before cleanup: {initial_files}")
        print(f"📊 Files after cleanup:  {final_files}")
        print(f"📦 Files archived:       {self.files_compressed}")
        print(f"💾 Space saved:          {space_saved_mb:.1f} MB")
        print(f"✨ Reduction:            {((initial_files - final_files) / initial_files * 100):.1f}%")
        
        self.list_remaining_files()
        
        print("\n💡 Your site is now clean and organized!")
        print("📦 All backups and development files are safely archived in 'archived-files/'")
        print("🚀 Ready for production deployment!")

if __name__ == "__main__":
    cleanup = WebsiteCleanup()
    cleanup.run_cleanup()
